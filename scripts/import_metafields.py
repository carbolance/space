#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Imports product Markdown sections into Shopify product metafields.

Env vars:
  SHOPIFY_STORE           (e.g., "carbolance")
  SHOPIFY_API_VERSION     (e.g., "2024-07")
  SHOPIFY_ACCESS_TOKEN    (Admin API access token)
Optional:
  SHOPIFY_PROTOCOL        (default "https")

Map Markdown -> metafields by editing FIELD_MAP below.

Usage:
  python scripts/import_metafields.py --handle premium-long-sleeve-t-shirt-midnight-black-classic --file products/premium-long-sleeve-midnight-black.md
"""
import os, sys, argparse, re, json
try:
    import requests
except Exception:
    requests = None

FIELD_MAP = {
    "Tagline":       ("copy", "tagline"),
    "Description":   ("copy", "description"),
    "Features":      ("copy", "features_md"),
    "Materials & Care": ("copy", "materials_care_md"),
    "Fit":           ("copy", "fit_md"),
    "SEO.Meta Title": ("seo", "meta_title"),
    "SEO.Meta Description": ("seo", "meta_description"),
}

H2_RE = re.compile(r'^##\s+(.+)$', re.M)

def split_sections(md):
    sections = {}
    matches = list(H2_RE.finditer(md))
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(md)
        sections[title] = md[start:end].strip()
    return sections

def get_product_by_handle(store, version, token, handle, protocol="https"):
    if requests is None:
        raise RuntimeError("The 'requests' library is required to call the Shopify API.")
    url = f"{protocol}://{store}.myshopify.com/admin/api/{version}/products.json?handle={handle}"
    r = requests.get(url, headers={"X-Shopify-Access-Token": token})
    r.raise_for_status()
    data = r.json().get("products", [])
    return data[0] if data else None

def set_metafield(store, version, token, owner_id, namespace, key, value, value_type="single_line_text_field", protocol="https"):
    if requests is None:
        raise RuntimeError("The 'requests' library is required to call the Shopify API.")
    url = f"{protocol}://{store}.myshopify.com/admin/api/{version}/metafields.json"
    payload = {"metafield": {"namespace": namespace, "key": key, "type": value_type, "owner_id": owner_id, "owner_resource": "product", "value": value}}
    r = requests.post(url, json=payload, headers={"X-Shopify-Access-Token": token})
    r.raise_for_status()
    return r.json()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--handle", required=True, help="Shopify product handle")
    ap.add_argument("--file", required=True, help="Markdown file path")
    args = ap.parse_args()

    store = os.environ.get("SHOPIFY_STORE")
    version = os.environ.get("SHOPIFY_API_VERSION", "2024-07")
    token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    protocol = os.environ.get("SHOPIFY_PROTOCOL", "https")

    if not (store and token):
        print("Missing SHOPIFY_STORE or SHOPIFY_ACCESS_TOKEN env vars.", file=sys.stderr)
        sys.exit(2)

    with open(args.file, "r", encoding="utf-8") as f:
        md = f.read()

    sections = split_sections(md)

    prod = get_product_by_handle(store, version, token, args.handle, protocol)
    if not prod:
        print(f"Product with handle '{args.handle}' not found.", file=sys.stderr)
        sys.exit(2)
    owner_id = prod["id"]

    for k, (ns, key) in FIELD_MAP.items():
        if k.startswith("SEO."):
            base = "SEO"
            label = k.split(".", 1)[1]  # "Meta Title" or "Meta Description"
            content = sections.get(base, "")
            value = ""
            for line in content.splitlines():
                line = line.strip()
                if line.lower().startswith(f"meta {label.lower()}:"):
                    value = line.split(":", 1)[1].strip()
                    break
        else:
            value = sections.get(k, "")
        if not value:
            continue
        ftype = "multi_line_text_field" if key.endswith("_md") else "single_line_text_field"
        set_metafield(store, version, token, owner_id, ns, key, value, ftype, protocol)

    print("Import complete.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
