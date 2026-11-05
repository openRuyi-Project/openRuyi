# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global lo_version 26.8.2.2

Name:           pentaho-libfonts
Version:        1.1.6
Release:        %autorelease
Summary:        Font registry and metrics for Pentaho Reporting
License:        LGPL-2.1-only
URL:            https://github.com/pentaho/pentaho-reporting
#!RemoteAsset:  sha256:e0531091787c0f16c83965fdcbc49162c059d7f0c64669e7f119699321549743
Source0:        https://downloads.sourceforge.net/project/jfreereport/02.%20Libraries/%{version}-stable/libfonts-%{version}.zip
BuildArch:      noarch

# Applied by the LibreOffice external project for this source release.
#!RemoteAsset:  sha256:8980ba27dc14ba20a9f78ccf3c5612dbafdb7add66a95e75a0501bfddd82e765
Patch0:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/common_build.patch
# LibreOffice upstream patch.
#!RemoteAsset:  sha256:cd1450a798a26e75d24d07beffe5d5e43ab765353718ff59dce7816f4f3b260e
Patch1:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/libfonts-1.1.6-deprecated.patch
# LibreOffice upstream patch.
#!RemoteAsset:  sha256:690f27969efd56cb7f4458e77f20cb75fc37c5a838c24b27c4a95d31090db479
Patch2:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/libfonts-1.1.3-remove-commons-logging.patch.1

BuildRequires:  ant
# TrueTypeFontRegistry asks Java2D for its available system font families.
BuildRequires:  fontconfig
BuildRequires:  fonts-dejavu
BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4
BuildRequires:  unzip
BuildRequires:  itext-birt
BuildRequires:  pentaho-libbase
BuildRequires:  pentaho-libloader
Requires:       fontconfig
Requires:       itext-birt
# Java2D needs a physical fallback face when enumerating or laying out system fonts.
Requires:       fonts-dejavu
Requires:       pentaho-libbase
Requires:       pentaho-libloader

%description
LibFonts supplies built-in PDF and TrueType font metrics for reports.

%prep
%autosetup -N -c
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete
sed -i 's/\r$//' common_build.xml
%patch -P 0 -p2
%patch -P 1 -p2
%patch -P 2 -p1
mkdir -p lib
ln -s %{_datadir}/java/itext-birt.jar lib/itext-birt.jar
ln -s %{_datadir}/java/libbase.jar lib/libbase.jar
ln -s %{_datadir}/java/libloader.jar lib/libloader.jar

%build
ant -nouserlib -f build.xml -Dbuild.label=%{version} \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Dantcontrib.available=true -Dbuild.id=10682 -Dproject.revision=%{version} \
    -Ditext-birt.jar=%{_datadir}/java/itext-birt.jar \
    -Dlibbase.jar=%{_datadir}/java/libbase.jar \
    -Dlibloader.jar=%{_datadir}/java/libloader.jar jar
printf 'Class-Path: itext-birt.jar libbase.jar libloader.jar\n' > system-jars.mf
jar --update --file dist/libfonts-%{version}.jar --manifest system-jars.mf

%install
install -Dpm644 dist/libfonts-%{version}.jar %{buildroot}%{_datadir}/java/libfonts.jar

%check
# Run all three upstream font suites.
mkdir classes-test
find test -name '*.java' | sort > test.sources
cp=dist/libfonts-%{version}.jar:%{_datadir}/java/itext-birt.jar:%{_datadir}/java/libbase.jar:%{_datadir}/java/libloader.jar
tc=$cp:%{_datadir}/java/junit4.jar
javac --release 8 -encoding UTF-8 -cp "$tc" -d classes-test @test.sources
java -Djava.awt.headless=true -cp "classes-test:test:$tc" org.junit.runner.JUnitCore \
    org.pentaho.reporting.libraries.fonts.encoding.CodePointBufferTest \
    org.pentaho.reporting.libraries.fonts.text.GraphemeClusterProducerTest \
    org.pentaho.reporting.libraries.fonts.truetype.TrueTypeFontRegistryTest

%files
%doc README.txt
%license licence-LGPL.txt
%{_datadir}/java/libfonts.jar

%changelog
%autochangelog
