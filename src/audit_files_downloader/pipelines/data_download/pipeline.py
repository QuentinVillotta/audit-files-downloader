from kedro.pipeline import Pipeline, node, pipeline
from audit_files_downloader.pipelines.data_download import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                nodes.extract_raw_data_from_api,
                inputs=[
                    "00_kobo_api_raw_data",
                    "params:api_data_key"
                ],
                outputs="01_raw_data"
            ),
            node(
                nodes.extract_audit_url,
                inputs=[
                    "01_raw_data",
                    "params:raw_data_survey_id",
                    "params:api_audit_location_key",
                    "params:api_audit_url_key"
                ],
                outputs="tmp_audit_url_df"
            ),
            node(
                nodes.extract_audit_files,
                inputs=[
                    "tmp_audit_url_df",
                    "params:raw_data_survey_id",
                    "params:kobo_credentials",
                    "params:dask_nb_worker",
                    "params:dask_nb_thread_per_worker"
                ],
                outputs="01_raw_audit"
            )
        ]
    )
