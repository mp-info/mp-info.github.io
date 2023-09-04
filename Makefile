-include .env
export

dl:
	# curl -O https://raw.githubusercontent.com/fortierq/scripts/main/cours/dl_nb.py
	python3 dl_nb.py ${TOKEN}
run:
	docker run -it --rm -p 8001:8000 -v $(shell pwd):/book/ qfortier/jb-addnote
git_rm:
	git rm --cached --ignore -unmatch
