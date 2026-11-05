# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global lo_version 26.8.2.2

Name:           pentaho-libformula
Version:        1.1.7
Release:        %autorelease
Summary:        OpenFormula evaluation for Pentaho Reporting
License:        LGPL-2.1-only
URL:            https://github.com/pentaho/pentaho-reporting
#!RemoteAsset:  sha256:5826d1551bf599b85742545f6e01a0079b93c1b2c8434bf409eddb3a29e4726b
Source0:        https://downloads.sourceforge.net/project/jfreereport/02.%20Libraries/%{version}-stable/libformula-%{version}.zip
# Upstream LibreOffice patches for this component.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/external/jfreereport/UnpackedTarball_jfreereport_libformula.mk
#!RemoteAsset:  sha256:8980ba27dc14ba20a9f78ccf3c5612dbafdb7add66a95e75a0501bfddd82e765
Source1:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/common_build.patch#/2000-common_build.patch
#!RemoteAsset:  sha256:65e43309af08e00dfa36e2f143e94876c93774e09550e7d65e4c474bb6d64bf9
Source2:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/libformula-time-notz.patch#/2001-libformula-time-notz.patch
#!RemoteAsset:  sha256:e60bdd7fcf43bc17d15b54028d3e41c15a1dddf98bcb3fb33bdc5c5c770a86d1
Source3:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/libformula-seconds_rounding.patch.1#/2002-libformula-seconds_rounding.patch
#!RemoteAsset:  sha256:6437e52ecb2691f806799f0a53e5412c508c5ec77c8c50628b8f7f1fccba90ee
Source4:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/libformula-minutes_truncation.patch.1#/2003-libformula-minutes_truncation.patch
#!RemoteAsset:  sha256:b1425e58c3910a133315816c3f106c745a332c9a28265b696cb43091b0cf7abe
Source5:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/libformula-datevalue_truncation.patch.1#/2004-libformula-datevalue_truncation.patch
#!RemoteAsset:  sha256:e5f8dd5d9e0bd69c91d2e217fc826a365cae35cdcd6b7666b3780d4994a87134
Source6:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/libformula-1.1.3-remove-commons-logging.patch.1#/2005-libformula-1.1.3-remove-commons-logging.patch
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip
BuildRequires:  junit4
BuildRequires:  pentaho-libbase
Requires:       pentaho-libbase

%patchlist
%{SOURCE1}
%{SOURCE2}
%{SOURCE3}
%{SOURCE4}
%{SOURCE5}
%{SOURCE6}
# Downstream precision fix for the upstream minute truncation change.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/external/jfreereport/patches/libformula-minutes_truncation.patch.1
2006-preserve-serial-date-minute-boundaries.patch

%description
LibFormula parses and evaluates spreadsheet-style formulas in reports.

%prep
%autosetup -N -c
# Build all classes from source, including the dependencies used by Ant.
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete
sed -i 's/\r$//' common_build.xml
# Upstream patch paths use different strip levels; apply each contiguous group in order.
%autopatch -p2 -m0 -M1
%autopatch -p1 -m2 -M6
mkdir -p lib
ln -s %{_datadir}/java/libbase.jar lib/libbase.jar

%build
ant -nouserlib -f build.xml -Dbuild.label=%{version} \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Dantcontrib.available=true -Dbuild.id=10682 -Dproject.revision=%{version} jar

%install
install -Dpm644 dist/libformula-%{version}.jar %{buildroot}%{_datadir}/java/libformula.jar

%check
# Run the upstream JUnit regression suites with deterministic locale and time zone.
mkdir classes-test
find test -name '*.java' | sort > test.sources
javac --release 8 -encoding UTF-8 -cp dist/libformula-%{version}.jar:%{_datadir}/java/libbase.jar:%{_datadir}/java/junit4.jar -d classes-test @test.sources
classes=$(while read -r file; do
    if grep -Eq 'public[[:space:]]+class[[:space:]]+' "$file" && grep -Eq 'public[[:space:]]+void[[:space:]]+test' "$file"; then
        echo "$file"
    fi
done < test.sources | sed -e 's|^test/||' -e 's|/|.|g' -e 's/[.]java$//')
test -n "$classes"
java -Djava.awt.headless=true -Duser.language=en -Duser.country=US -Duser.timezone=UTC \
    -cp classes-test:dist/libformula-%{version}.jar:%{_datadir}/java/libbase.jar:%{_datadir}/java/junit4.jar org.junit.runner.JUnitCore $classes > upstream-tests.log
cat upstream-tests.log

%files
%doc README.txt
%license licence-LGPL.txt
%{_datadir}/java/libformula.jar

%changelog
%autochangelog
