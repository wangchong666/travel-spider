FROM ubuntu

MAINTAINER Wang Chong <w420050757@gmail.com>

ENTRYPOINT ["/runtime/entrypoint.sh"]
CMD ["scrapy"]
