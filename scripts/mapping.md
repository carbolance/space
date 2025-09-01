# Markdown → Shopify Metafields Mapping

| Markdown Section       | Namespace | Key               | Type                   | Notes |
|------------------------|-----------|-------------------|------------------------|-------|
| Tagline                | copy      | tagline           | single_line_text_field | Short one-liner. |
| Description            | copy      | description       | multi_line_text_field  | Accepts Markdown. |
| Features               | copy      | features_md       | multi_line_text_field  | Bullet list in Markdown. |
| Materials & Care       | copy      | materials_care_md | multi_line_text_field  | Accepts Markdown. |
| Fit                    | copy      | fit_md            | multi_line_text_field  | Accepts Markdown. |
| SEO → Meta Title       | seo       | meta_title        | single_line_text_field | From line `Meta Title:`. |
| SEO → Meta Description | seo       | meta_description  | single_line_text_field | From line `Meta Description:`. |
