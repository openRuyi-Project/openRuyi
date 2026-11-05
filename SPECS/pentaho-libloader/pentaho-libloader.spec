# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global lo_version 26.8.2.2

Name:           pentaho-libloader
Version:        1.1.6
Release:        %autorelease
Summary:        Resource loader for Pentaho Reporting
License:        LGPL-2.1-only
URL:            https://github.com/pentaho/pentaho-reporting
#!RemoteAsset:  sha256:3d853b19b1d94a6efa69e7af90f7f2b09ecf302913bee3da796c15ecfebcfac8
Source0:        https://downloads.sourceforge.net/project/jfreereport/02.%20Libraries/%{version}-stable/libloader-%{version}.zip
# Applied by the LibreOffice external project for this source release.
#!RemoteAsset:  sha256:8980ba27dc14ba20a9f78ccf3c5612dbafdb7add66a95e75a0501bfddd82e765
Source1:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/common_build.patch#/2000-common_build.patch
# LibreOffice upstream patch.
#!RemoteAsset:  sha256:a231318b1877fd418c7f27eab7a0fc0178be812f96b593f207f50ee1902ab99e
Source2:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/libloader-1.1.6-deprecated.patch#/2001-libloader-1.1.6-deprecated.patch
# LibreOffice upstream patch.
#!RemoteAsset:  sha256:f6266a81995e3ad7dd491dd9e9efefd5a98471542d0d3d0699a99fcad51e98a7
Source3:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/libloader-1.1.3-remove-commons-logging.patch.1#/2002-libloader-1.1.3-remove-commons-logging.patch
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4
BuildRequires:  unzip
BuildRequires:  batik
BuildRequires:  ehcache
BuildRequires:  pentaho-libbase
BuildRequires:  pentaho-libpixie
BuildRequires:  xml-commons-apis-ext
Requires:       batik
Requires:       ehcache
Requires:       pentaho-libbase
Requires:       pentaho-libpixie
Requires:       xml-commons-apis-ext

%patchlist
%{SOURCE1}
%{SOURCE2}
%{SOURCE3}
# Downstream fix for SVG resource detection and rendering through the public resource manager.
# https://github.com/pentaho/pentaho-reporting/tree/master/libraries/libloader
2003-match-resource-file-extensions.patch
# Downstream fix for SVG resource detection and rendering through the public resource manager.
# https://github.com/pentaho/pentaho-reporting/tree/master/libraries/libloader
2004-render-svg-before-reading-pixels.patch

%description
LibLoader loads and caches typed report resources, including SVG and WMF images.

%prep
%autosetup -N -c
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete
sed -i 's/\r$//' common_build.xml
# Upstream patch paths use different strip levels; apply each contiguous group in order.
%autopatch -p2 -m0 -M1
%autopatch -p1 -m2 -M4
mkdir -p lib
ln -s %{_datadir}/java/batik-all.jar lib/batik-all.jar
ln -s %{_datadir}/java/ehcache.jar lib/ehcache.jar
ln -s %{_datadir}/java/libbase.jar lib/libbase.jar
ln -s %{_datadir}/java/libpixie.jar lib/libpixie.jar
ln -s %{_datadir}/java/xml-apis-ext.jar lib/xml-apis-ext.jar

%build
ant -nouserlib -f build.xml -Dbuild.label=%{version} \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Dantcontrib.available=true -Dbuild.id=10682 -Dproject.revision=%{version} \
    -Dbatik-all.jar=%{_datadir}/java/batik-all.jar \
    -Dehcache.jar=%{_datadir}/java/ehcache.jar \
    -Dlibbase.jar=%{_datadir}/java/libbase.jar \
    -Dlibpixie.jar=%{_datadir}/java/libpixie.jar \
    -Dxml-apis-ext.jar=%{_datadir}/java/xml-apis-ext.jar jar
printf 'Class-Path: batik-all.jar ehcache.jar libbase.jar libpixie.jar xml-apis-ext.jar\n' > system-jars.mf
jar --update --file dist/libloader-%{version}.jar --manifest system-jars.mf

%install
install -Dpm644 dist/libloader-%{version}.jar %{buildroot}%{_datadir}/java/libloader.jar

%check
# Run key construction and derivation. The archived serialization tests expect an older wire format.
mkdir classes-test
find test -name '*.java' | sort > test.sources
cp=dist/libloader-%{version}.jar:%{_datadir}/java/batik-all.jar:%{_datadir}/java/ehcache.jar:%{_datadir}/java/libbase.jar:%{_datadir}/java/libpixie.jar:%{_datadir}/java/xml-apis-ext.jar
tc=$cp:%{_datadir}/java/junit4.jar
javac --release 8 -encoding UTF-8 -cp "$tc" -d classes-test @test.sources
java -Djava.awt.headless=true -cp "classes-test:test:$tc" org.junit.runner.JUnitCore \
    org.pentaho.reporting.libraries.resourceloader.TestResourceKey

%files
%doc README.txt
%license licence-LGPL.txt
%{_datadir}/java/libloader.jar

%changelog
%autochangelog
