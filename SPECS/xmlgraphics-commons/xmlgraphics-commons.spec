# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xmlgraphics-commons
Version:        2.12
Release:        %autorelease
Summary:        Shared image and graphics support for Apache XML Graphics
License:        Apache-2.0
URL:            https://xmlgraphics.apache.org/commons/
VCS:            git:https://github.com/apache/xmlgraphics-commons.git
#!RemoteAsset:  sha256:5d6e8ead658006746769a44ac6f0f8744cda1610a1573be037da6eb84c308f29
Source0:        https://archive.apache.org/dist/xmlgraphics/commons/source/xmlgraphics-commons-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4
BuildRequires:  slf4j-jcl
BuildRequires:  slf4j-jdk14
Requires:       slf4j-jcl
Requires:       slf4j-jdk14

%description
XML Graphics Commons supplies color spaces, image loaders and writers,
Java2D drawing support and PostScript utilities.

%prep
%autosetup -n xmlgraphics-commons-%{version}

%build
mkdir classes
find src/main/java -name '*.java' | sort > sources.list
javac --release 11 -encoding UTF-8 -cp %{_datadir}/java/jcl-over-slf4j.jar -d classes @sources.list
cp -rp src/main/resources/. classes/
printf 'Class-Path: jcl-over-slf4j.jar slf4j-jdk14.jar\n' > manifest.mf
jar --create --file xmlgraphics-commons.jar --manifest manifest.mf -C classes .

%install
install -Dpm644 xmlgraphics-commons.jar %{buildroot}%{_datadir}/java/xmlgraphics-commons.jar

%check
# Run the self-contained tests from upstream StandardTestSuite.
# ImageEncodingHelperTestCase needs Mockito, which the target repository does not provide.
mkdir classes-test
cp=xmlgraphics-commons.jar:%{_datadir}/java/jcl-over-slf4j.jar:%{_datadir}/java/slf4j-jdk14.jar:%{_datadir}/java/junit4.jar
suites="org.apache.xmlgraphics.util.io.Base64Test
org.apache.xmlgraphics.util.io.ASCII85InputStreamTestCase
org.apache.xmlgraphics.util.io.ASCII85OutputStreamTestCase
org.apache.xmlgraphics.image.codec.png.PNGEncoderTestCase
org.apache.xmlgraphics.util.ServiceTestCase
org.apache.xmlgraphics.util.ClasspathResourceTestCase
org.apache.xmlgraphics.ps.PSEscapeTestCase
org.apache.xmlgraphics.ps.dsc.events.DSCValueParserTestCase
org.apache.xmlgraphics.ps.dsc.tools.DSCToolsTestCase
org.apache.xmlgraphics.ps.dsc.ListenerTestCase
org.apache.xmlgraphics.util.UnitConvTestCase"
for suite in $suites; do printf 'src/test/java/%s.java\n' "$(echo "$suite" | tr . /)"; done > test.sources
javac --release 11 -encoding UTF-8 -cp "$cp" -sourcepath src/test/java -d classes-test @test.sources
cp -rp src/test/resources/. classes-test/
java -Djava.awt.headless=true -cp "classes-test:$cp" org.junit.runner.JUnitCore $suites

%files
%license LICENSE NOTICE
%{_datadir}/java/xmlgraphics-commons.jar

%changelog
%autochangelog
