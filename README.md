# QA LLM-API

QA LLM-API is an Rest API wrapper built on the top of langchain APIs. It exposes a POST api `/api/qa` which takes Question file(json) format and Contextual Data file(json or pdf) built using Python Fast API

## Installation

Use docker to setup

```bash
docker build -t llm-api .
docker run -p 8000:8000 llm-api
```

## Usage

You can go to `http://0.0.0.0:8000/docs` to interact using Swagger

OR

```bash
curl -X 'POST' \
  'http://0.0.0.0:8000/api/qa' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'questions_file=@google_security_questions.json;type=application/json' \
  -F 'document_file=@google_security_wp.pdf;type=application/pdf'
```

## Support

For any suggestions/feedback, Drop me an Email at **shivam.singhal212@gmail.com**

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
