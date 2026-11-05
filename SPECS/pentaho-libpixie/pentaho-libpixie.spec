# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pentaho-libpixie
Version:        1.1.6
Release:        %autorelease
Summary:        Windows Metafile reader for Pentaho Reporting
License:        LGPL-2.1-only
URL:            https://github.com/pentaho/pentaho-reporting
#!RemoteAsset:  sha256:d353bbf896b541fd8b0f0ed1b5cb26ed41b8e93b102f9e92f2936d93f08ab737
Source0:        https://downloads.sourceforge.net/project/jfreereport/02.%20Libraries/%{version}-stable/libpixie-%{version}.zip
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  pentaho-libbase
BuildRequires:  slf4j-jcl
BuildRequires:  slf4j-jdk14
BuildRequires:  unzip
Requires:       pentaho-libbase
Requires:       slf4j-jcl
Requires:       slf4j-jdk14

%description
Pixie reads Windows Metafile records and renders vector graphics for the
Pentaho Reporting resource loader.

%prep
%autosetup -N -c
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete

%build
mkdir classes
find source -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -cp %{_datadir}/java/libbase.jar:%{_datadir}/java/jcl-over-slf4j.jar \
    -d classes @sources.list
(cd source && find . -type f ! -name '*.java' -exec cp --parents -p {} ../classes/ \;)
printf 'Class-Path: libbase.jar jcl-over-slf4j.jar slf4j-jdk14.jar\n' > manifest.mf
jar --create --file libpixie.jar --manifest manifest.mf -C classes .

%install
install -Dpm644 libpixie.jar %{buildroot}%{_datadir}/java/libpixie.jar

# The upstream source distribution does not include an automated test suite.

%files
%doc README.txt
%license licence-LGPL.txt
%{_datadir}/java/libpixie.jar

%changelog
%autochangelog
