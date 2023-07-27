FROM scratch

# Metadata params
ARG BUILD_DATE
ARG VERSION
ARG VCS_URL
ARG VCS_REF
ARG TARBALL
ARG RELEASE_DESCRIPTION

# https://github.com/opencontainers/image-spec/blob/master/annotations.md
LABEL org.opencontainers.image.created=$BUILD_DATE \
      org.opencontainers.image.source=$VCS_URL \
      org.opencontainers.image.revision=$VCS_REF \
      org.opencontainers.image.vendor='Offensive Security' \
      org.opencontainers.image.version=$VERSION \
      org.opencontainers.image.title="Kali Linux ($RELEASE_DESCRIPTION release)" \
      org.opencontainers.image.description="Official Kali Linux docker image for $RELEASE_DESCRIPTION" \
      org.opencontainers.image.url='https://www.kali.org/' \
      org.opencontainers.image.authors="Kali Developers <devel@kali.org>"

ADD $TARBALL /

CMD ["bash"]
