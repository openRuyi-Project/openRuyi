# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           docbook-xsl
Version:        1.79.2
Release:        %autorelease
Summary:        Norman Walsh's XSL stylesheets for DocBook XML & DocBook 5.X
License:        LicenseRef-DMIT AND MIT AND MPL-1.1
URL:            https://github.com/docbook/xslt10-stylesheets
#!RemoteAsset
Source0:        %{url}/releases/download/release/%{version}/docbook-xsl-%{version}.tar.bz2
#!RemoteAsset
Source1:        %{url}/releases/download/release/%{version}/docbook-xsl-doc-%{version}.tar.bz2
# Build Script for convienience
Source2:        %{name}.Makefile
BuildArch:      noarch

# For compatibility
Provides:       docbook-xsl-ns

Requires:       xml-common
Requires(post): libxml2
Requires(postun): libxml2

%description
These XSL stylesheets allow you to transform any DocBook XML document or
DocBook 5 document to other formats, such as HTML, FO, and XHMTL. They
are highly customizable. For more information see W3C page about XSL.

%prep
%setup -c -T -n docbook-xsl-%{version}
tar jxf %{SOURCE0}
mv docbook-xsl-%{version}/* .
pushd ..
tar jxf %{SOURCE1}
popd

# Remove .gitignore files
rm -rf $(find -name '.gitignore' -type f)

# Remove ant buildsystem
find . -name build.xml -delete

# Remove binary JAR files
rm -f extensions/*.jar
rm -fr tools/

# Make ruby scripts executable
chmod +x epub/bin/dbtoepub

# Remove misc
rm slides/slidy/scripts/slidy.js.gz
rm roundtrip/template.dot

# Copy our Makefile
cp -p %{SOURCE2} Makefile

# fix of non UTF-8 files rpmlint warnings
for fhtml in $(find ./doc -name '*.html' -type f)
do
 iconv -f ISO-8859-1 -t UTF-8 "$fhtml" -o "$fhtml".tmp
 mv -f "$fhtml".tmp "$fhtml"
 sed -i 's/charset=ISO-8859-1/charset=UTF-8/' "$fhtml"
done

for f in $(find -name "*'*")
do
 mv -v "$f" $(echo "$f" | tr -d "'")
done

%build
# No build for ya

%install
# Version 4
make install BINDIR=%{buildroot}%{_bindir} DESTDIR=%{buildroot}%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}
cp -a VERSION.xsl %{buildroot}%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/VERSION.xsl
ln -s xsl-stylesheets-%{version} \
        %{buildroot}%{_datadir}/sgml/docbook/xsl-stylesheets
# Don't ship the extensions
rm -rf %{buildroot}%{_datadir}/sgml/docbook/xsl-stylesheets/extensions/*
# Version 5
mkdir -p %{buildroot}%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}
cp -a [[:lower:]]* %{buildroot}%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}/
cp -a VERSION %{buildroot}%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}/VERSION.xsl
ln -s VERSION.xsl \
%{buildroot}%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}/VERSION
ln -s xsl-ns-stylesheets-%{version} \
 %{buildroot}%{_datadir}/sgml/docbook/xsl-ns-stylesheets
# Don't ship install shell script.
rm -rf %{buildroot}%{_datadir}/sgml/docbook/xsl-ns-stylesheets/install.sh

%post
CATALOG=%{_sysconfdir}/xml/catalog
# Version 4
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://cdn.docbook.org/release/xsl-nons/%{version}" \
 "file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://cdn.docbook.org/release/xsl-nons/%{version}" \
 "file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://cdn.docbook.org/release/xsl-nons/current/" \
 "file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://cdn.docbook.org/release/xsl-nons/current/" \
 "file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}" $CATALOG
#keep the old one sourceforge URIs at least temporarily
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://docbook.sourceforge.net/release/xsl/current" \
 "file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://docbook.sourceforge.net/release/xsl/current" \
 "file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}" $CATALOG
# Version 5
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://cdn.docbook.org/release/xsl/%{version}" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://cdn.docbook.org/release/xsl/%{version}" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://cdn.docbook.org/release/xsl/current/" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://cdn.docbook.org/release/xsl/current/" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG

%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://docbook.sourceforge.net/release/xsl-ns/current" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://docbook.sourceforge.net/release/xsl-ns/current" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG

%postun
# Version 4
# remove entries only on removal of package
if [ "$1" = 0 ]; then
  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del \
   "file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}" $CATALOG
fi
# Version 5
# remove entries only on removal of package
if [ "$1" = 0 ]; then
  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del \
   "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
fi

%files
%doc BUGS
%doc README COPYING
%doc TODO NEWS
%doc RELEASE-NOTES.*
# Version 4
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}
%{_datadir}/sgml/docbook/xsl-stylesheets
# Version 5
%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}
%{_datadir}/sgml/docbook/xsl-ns-stylesheets

%changelog
%autochangelog
