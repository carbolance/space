#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exports product metafields to JSON for inspection/backups.

Env:
  SHOPIFY_STORE, SHOPIFY_API_VERSION, SHOPIFY_ACCESS_TOKEN, SHOPIFY_PROTOCOL(optional)

Usage:
  python scripts/export_metafields.py --handle premium-long-sleeve-t-shirt-midnight-black-classic > meta.json
"""
import os, sys, argparse, json
try:
    import requests
except Exception:
    requests = None

def list_metafields(store, version, token, owner_id, protocol="https"):
    if requests is None:
        raise RuntimeError("The 'requests' library is required to call the Shopify API.")
    url = f"{protocol}://{store}.myshopify.com/admin/api/{version}/metafields.json?metafield[owner_id]={owner_id}&metafield[owner_resource]=product"
    r = requests.get(url, headers={"X-Shopify-Access-Token": token})
    r.raise_for_status()
    return r.json().get("metafields", [])

def main():
    ap = argparse.ArgumentParser()
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--product-id", type=int, help="Shopify product ID")
    group.add_argument("--handle", help="Shopify product handle")
    args = ap.parse_args()

    store = os.environ.get("SHOPIFY_STORE")
    version = os.environ.get("SHOPIFY_API_VERSION", "2024-07")
    token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    protocol = os.environ.get("SHOPIFY_PROTOCOL", "https")

    if not (store and token):
        print("Missing SHOPIFY_STORE or SHOPIFY_ACCESS_TOKEN env vars.", file=sys.stderr)
        sys.exit(2)

    if args.handle:
        if requests is None:
            raise RuntimeError("The 'requests' library is required to call the Shopify API.")
        url = f"{protocol}://{store}.myshopify.com/admin/api/{version}/products.json?handle={args.handle}"
        r = requests.get(url, headers={"X-Shopify-Access-Token": token})
        r.raise_for_status()
        prods = r.json().get("products", [])
        if not prods:
            print(f"No product found with handle {args.handle}", file=sys.stderr)
            sys.exit(2)
        owner_id = prods[0]["id"]
    else:
        owner_id = args.product_id

    mfs = list_metafields(store, version, token, owner_id, protocol)
    print(json.dumps(mfs, indent=2))

if __name__ == "__main__":
    sys.exit(main())
