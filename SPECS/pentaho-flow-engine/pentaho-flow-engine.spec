# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global lo_version 26.8.2.2

Name:           pentaho-flow-engine
Version:        0.9.4
Release:        %autorelease
Summary:        Flow reporting engine for LibreOffice Report Builder
License:        LGPL-2.1-or-later
URL:            https://github.com/pentaho/pentaho-reporting
#!RemoteAsset:  sha256:233f66e8d25c5dd971716d4200203a612a407649686ef3b52075d04b4c9df0dd
Source0:        https://downloads.sourceforge.net/project/jfreereport/10.%20Flow%20Engine/%{version}/flow-engine-%{version}.zip
BuildArch:      noarch

# Applied by the LibreOffice external project for this source release.
#!RemoteAsset:  sha256:b8a56537fe6113954a1ede79b48cd6482e6fced239c775edf56de6ff771e6617
Patch0:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/flow-engine.patch
# LibreOffice upstream patch.
#!RemoteAsset:  sha256:cf75911407cddfe08dd8f7b6ea21b0dd2b3a7188d8df1bd488ece4e3d548d2f3
Patch1:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/flow-engine_date_is_datetime.patch.1
# LibreOffice upstream patch.
#!RemoteAsset:  sha256:b1d479e1ebd8b80d2683dfc76529b6d4abb8bf10d5b0c8d7a3700e49467d3c49
Patch2:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/pentaho-reporting-flow-engine-0.9.4-remove-commons-logging.patch.1

BuildRequires:  ant
BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4
BuildRequires:  unzip
BuildRequires:  pentaho-libbase
BuildRequires:  pentaho-libformula
BuildRequires:  pentaho-liblayout
BuildRequires:  pentaho-libloader
BuildRequires:  pentaho-libserializer
BuildRequires:  pentaho-libxml
Requires:       pentaho-libbase
Requires:       pentaho-libformula
Requires:       pentaho-liblayout
Requires:       pentaho-libloader
Requires:       pentaho-libserializer
Requires:       pentaho-libxml

%description
The Pentaho flow engine combines data sources, expressions and page layout to generate reports.

%prep
%autosetup -N -c
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete
sed -i 's/\r$//' build.xml
%patch -P 0 -p2
%patch -P 1 -p1
%patch -P 2 -p1
mkdir -p lib
ln -s %{_datadir}/java/libbase.jar lib/libbase.jar
ln -s %{_datadir}/java/libformula.jar lib/libformula.jar
ln -s %{_datadir}/java/liblayout.jar lib/liblayout.jar
ln -s %{_datadir}/java/libloader.jar lib/libloader.jar
ln -s %{_datadir}/java/libserializer.jar lib/libserializer.jar
ln -s %{_datadir}/java/libxml.jar lib/libxml.jar

%build
ant -nouserlib -f build.xml -Dbuild.label=%{version} \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Dantcontrib.available=true -Dbuild.id=10682 -Dproject.revision=%{version} \
    -Dlibbase.jar=%{_datadir}/java/libbase.jar \
    -Dlibformula.jar=%{_datadir}/java/libformula.jar \
    -Dliblayout.jar=%{_datadir}/java/liblayout.jar \
    -Dlibloader.jar=%{_datadir}/java/libloader.jar \
    -Dlibserializer.jar=%{_datadir}/java/libserializer.jar \
    -Dlibxml.jar=%{_datadir}/java/libxml.jar jar
printf 'Class-Path: libbase.jar libformula.jar liblayout.jar libloader.jar libserializer.jar libxml.jar\n' > system-jars.mf
jar --update --file build/lib/flow-engine.jar --manifest system-jars.mf

%install
install -Dpm644 build/lib/flow-engine.jar %{buildroot}%{_datadir}/java/flow-engine.jar

%check
# Run both concrete upstream JUnit suites for report data and bean-backed data sources.
mkdir classes-test
find test -name '*.java' | sort > test.sources
cp=build/lib/flow-engine.jar:%{_datadir}/java/libbase.jar:%{_datadir}/java/libformula.jar:%{_datadir}/java/liblayout.jar:%{_datadir}/java/libloader.jar:%{_datadir}/java/libserializer.jar:%{_datadir}/java/libxml.jar
tc=$cp:%{_datadir}/java/junit4.jar
javac --release 8 -encoding UTF-8 -cp "$tc" -d classes-test @test.sources
java -Djava.awt.headless=true -cp "classes-test:test:$tc" org.junit.runner.JUnitCore \
    org.jfree.report.Pre397Test \
    org.jfree.report.modules.data.beans.StaticReportDataFactoryTest

%files
%doc README.txt
%license licence-LGPL.txt
%{_datadir}/java/flow-engine.jar

%changelog
%autochangelog
