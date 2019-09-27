import os
import glob
import argparse
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", dest="output", required=True)
    known_args, pipeline_args = parser.parse_known_args()
    output_file = "%s.txt" % known_args.output
    for filename in glob.glob(output_file+'*'):
        os.remove(filename)
    with beam.Pipeline(options=PipelineOptions(pipeline_args)) as p:
        sentence = ["coucou"]
        (
            p
            | 'create' >> beam.Create(sentence)
            | 'write' >> beam.io.WriteToText(output_file)
        )
