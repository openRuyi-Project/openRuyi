# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global tag release-48-2

Name:           cldr-emoji-annotation
Version:        48.2
Release:        %autorelease
Summary:        Emoji annotation files in CLDR
License:        Unicode-DFS-2016
URL:            https://unicode.org/cldr
VCS:            git:https://github.com/unicode-org/cldr.git
#!RemoteAsset:  sha256:d9b99299f3fbd3070b357612f4a4c4c64bff59ad7f05b4e636efdf1b60fe69f6
Source0:        https://github.com/unicode-org/cldr/archive/refs/tags/%{tag}.tar.gz
BuildArch:      noarch

%description
This package provides the emoji annotation file by language in CLDR.

%prep
%autosetup -n cldr-%{tag}

%install
ANNOTATION_DIR=common/annotations
CLDR_DIR=%{buildroot}%{_datadir}/unicode/cldr/$ANNOTATION_DIR
mkdir -p $CLDR_DIR
for xml in $ANNOTATION_DIR/*.xml; do
    install -pm 644 $xml $CLDR_DIR/
done

ANNOTATION_DERIVED_DIR=common/annotationsDerived
CLDR_DERIVED_DIR=%{buildroot}%{_datadir}/unicode/cldr/$ANNOTATION_DERIVED_DIR
mkdir -p $CLDR_DERIVED_DIR
for xml in $ANNOTATION_DERIVED_DIR/*.xml; do
    install -pm 644 $xml $CLDR_DERIVED_DIR/
done

DTD_DIR=common/dtd
CLDR_DTD_DIR=%{buildroot}%{_datadir}/unicode/cldr/$DTD_DIR
mkdir -p $CLDR_DTD_DIR
for dtd in $DTD_DIR/*.dtd; do
    install -pm 644 $dtd $CLDR_DTD_DIR/
done

# Generate pkgconfig file
mkdir -p %{buildroot}%{_datadir}/pkgconfig
cat > %{buildroot}%{_datadir}/pkgconfig/cldr-emoji-annotation.pc <<EOF
prefix=/usr

Name: cldr-emoji-annotations
Description: Annotation files in CLDR
Version: %{version}
EOF

%files
%license LICENSE
%{_datadir}/unicode/
%{_datadir}/pkgconfig/cldr-emoji-annotation.pc

%changelog
%autochangelog
