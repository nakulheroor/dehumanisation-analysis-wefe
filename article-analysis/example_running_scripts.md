# Running the analysis script with gemini API

1. Install python dependencies from `requirements_gemini.txt`. 
2. Set `GEMINI_API_KEY` in the `.env` file. 
3. Check that the rubric is present (e.g. `rubric_short_v2.md`), as well as the folder with the sampled articles in the input directory.
4. Run (inputs can be changed or made optional):

``` python3 analyze_articles_batch_api_gemini.py \
  --input-dir articles_all_txt_clean_sample \
  --output-dir articles_all_json_output_v2 \
  --rubric rubric_short_v2.md \
  --model gemini-3.1-flash-lite-preview \
  --batch-size 500 \
  --start-index 0 \
  --workers 2 
  ```

The output is: 

- one .json result per article in the output directory (in this exmaple `articles_all_json_output_v2`)
- batch_usage.jsonl: here you can analyze the intput and output tokens. 
- batch_errors.log: sometimes the models are not avalaible because of a high demand, so if it fails, it prints the reason why here. 

**Explanation**: 
- This script is to run a batch of size `batch-size`, starting at index `start-index`. This can be modified. Right now existing output files in the output directory are skipped, unless `--overwrite` is written. 
- If the output directory is not present it is automatically created. 
- The model can be modified with `--model` (you can also write for example `gemini-2.5-flash-lite`).
- Not sure what is the best way to setup `--workers`. Initially I added because the gpt version was very slow, but it's not so relevant for gemini.


