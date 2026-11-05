# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global lo_version 26.8.2.2

Name:           pentaho-liblayout
Version:        0.2.10
Release:        %autorelease
Summary:        CSS layout engine for Pentaho Reporting
License:        LGPL-2.1-or-later
URL:            https://github.com/pentaho/pentaho-reporting
#!RemoteAsset:  sha256:e1fb87f3f7b980d33414473279615c4644027e013012d156efa538bc2b031772
Source0:        https://downloads.sourceforge.net/project/jfreereport/10.%20Flow%20Engine/0.9.4/liblayout-%{version}.zip
BuildArch:      noarch

# Applied by the LibreOffice external project for this source release.
#!RemoteAsset:  sha256:d1a550f2eb793fd531ea3e6cc98dea9a665c866a3e8a0b9e6e949d45bf3b5f66
Patch0:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/liblayout.patch
# LibreOffice upstream patch.
#!RemoteAsset:  sha256:efd1f1ec77e52e2a1b6d6219992c46fa1a86c9ff0ce85c4848caeff33b207889
Patch1:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/liblayout-0.2.10-remove-commons-logging.patch.1

BuildRequires:  ant
BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4
BuildRequires:  unzip
BuildRequires:  pentaho-flute
BuildRequires:  pentaho-libbase
BuildRequires:  pentaho-libfonts
BuildRequires:  pentaho-libloader
BuildRequires:  pentaho-librepository
BuildRequires:  pentaho-libxml
BuildRequires:  java-sac
Requires:       pentaho-flute
Requires:       pentaho-libbase
Requires:       pentaho-libfonts
Requires:       pentaho-libloader
Requires:       pentaho-librepository
Requires:       pentaho-libxml
Requires:       java-sac

%description
LibLayout lays out styled elements and text for the reporting engine.

%prep
%autosetup -N -c
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete
sed -i 's/\r$//' build.xml
%patch -P 0 -p2
%patch -P 1 -p1
mkdir -p lib
ln -s %{_datadir}/java/flute.jar lib/flute.jar
ln -s %{_datadir}/java/libbase.jar lib/libbase.jar
ln -s %{_datadir}/java/libfonts.jar lib/libfonts.jar
ln -s %{_datadir}/java/libloader.jar lib/libloader.jar
ln -s %{_datadir}/java/librepository.jar lib/librepository.jar
ln -s %{_datadir}/java/libxml.jar lib/libxml.jar
ln -s %{_datadir}/java/sac.jar lib/sac.jar

%build
ant -nouserlib -f build.xml -Dbuild.label=%{version} \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Dantcontrib.available=true -Dbuild.id=10682 -Dproject.revision=%{version} \
    -Dflute.jar=%{_datadir}/java/flute.jar \
    -Dlibbase.jar=%{_datadir}/java/libbase.jar \
    -Dlibfonts.jar=%{_datadir}/java/libfonts.jar \
    -Dlibloader.jar=%{_datadir}/java/libloader.jar \
    -Dlibrepository.jar=%{_datadir}/java/librepository.jar \
    -Dlibxml.jar=%{_datadir}/java/libxml.jar \
    -Dsac.jar=%{_datadir}/java/sac.jar jar
# The default stylesheets are loaded by URL. The upstream Ant target copies only properties.
for css in initial html liblayout; do
    jar --update --file build/lib/liblayout.jar -C source "org/jfree/layouting/$css.css"
done
printf 'Class-Path: flute.jar libbase.jar libfonts.jar libloader.jar librepository.jar libxml.jar sac.jar\n' > system-jars.mf
jar --update --file build/lib/liblayout.jar --manifest system-jars.mf

%install
install -Dpm644 build/lib/liblayout.jar %{buildroot}%{_datadir}/java/liblayout.jar

%check
# Run the upstream element, table and geometry checks with their default CSS. The legacy text fixtures construct a renderer without a layout process.
mkdir classes-test
find test -name '*.java' | sort > test.sources
cp=build/lib/liblayout.jar:%{_datadir}/java/flute.jar:%{_datadir}/java/libbase.jar:%{_datadir}/java/libfonts.jar:%{_datadir}/java/libloader.jar:%{_datadir}/java/librepository.jar:%{_datadir}/java/libxml.jar:%{_datadir}/java/sac.jar
tc=$cp:%{_datadir}/java/junit4.jar
javac --release 8 -encoding UTF-8 -cp "$tc" -d classes-test @test.sources
java -Djava.awt.headless=true -cp "classes-test:test:$tc" org.junit.runner.JUnitCore \
    org.jfree.layouting.test.BlockAndInlineTest \
    org.jfree.layouting.test.DirtyTableTest \
    org.jfree.layouting.test.InlineBlockTest \
    org.jfree.layouting.test.MixInlineAndBlockTest \
    org.jfree.layouting.test.TableTest \
    org.jfree.layouting.test.WorldAPICrashTest \
    org.jfree.layouting.util.StrictGeomUtilityTest

%files
%doc README.txt
%license licence-LGPL.txt
%{_datadir}/java/liblayout.jar

%changelog
%autochangelog
