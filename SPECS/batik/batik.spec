# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           batik
Version:        1.20
Release:        %autorelease
Summary:        SVG DOM, rendering and JavaScript toolkit
License:        Apache-2.0
URL:            https://xmlgraphics.apache.org/batik/
VCS:            git:https://github.com/apache/xmlgraphics-batik.git
#!RemoteAsset:  sha256:95d46a238ecbbe8abe1c2957b0bdf09bf7d60cb844fa23dec0cf7b35525bfd53
Source0:        https://archive.apache.org/dist/xmlgraphics/batik/source/batik-src-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4
BuildRequires:  python3
BuildRequires:  java-sac
BuildRequires:  rhino
BuildRequires:  xml-commons-apis-ext
BuildRequires:  xmlgraphics-commons
Requires:       java-sac
Requires:       rhino
Requires:       xml-commons-apis-ext
Requires:       xmlgraphics-commons

%description
Batik parses SVG documents, builds their graphics trees, renders images and
provides the JavaScript integration used by SVG applications.

%prep
%autosetup -n batik-%{version}
# The source distribution carries library binaries. Use the system Java libraries.
find lib -type f -name '*.jar' -delete

%build
mkdir classes
# Follow batik-all's module order and the upstream Ant conditions on optional
# JACL and JPython interpreters. Rhino remains available for JavaScript.
%{__python3} - <<'MODULES'
from pathlib import Path
from shutil import copyfile
from xml.etree import ElementTree as ET
root=ET.parse("batik-all/pom.xml")
deps=root.findall("./{*}dependencies/{*}dependency")
modules=[d.findtext("{*}artifactId") for d in deps if d.findtext("{*}artifactId").startswith("batik-")]
assert {"batik-bridge","batik-script","batik-dom"} <= set(modules)
sources=[]
for name in modules:
    module=Path(name)/"src/main"
    sources.extend(str(p) for p in sorted((module/"java").rglob("*.java"))
                   if "jpython" not in p.parts and "jacl" not in p.parts)
    resources=module/"resources"
    for p in sorted(resources.rglob("*")):
        if not p.is_file(): continue
        relative=p.relative_to(resources)
        dest=Path("classes")/relative
        dest.parent.mkdir(parents=True,exist_ok=True)
        if relative.parts[:2]==("META-INF","services"):
            with dest.open("ab") as f: f.write(p.read_bytes()+b"\n")
        elif not dest.exists():
            copyfile(p,dest)
Path("sources.list").write_text("\n".join(sources)+"\n")
MODULES
cp=%{_datadir}/java/xml-apis-ext.jar:%{_datadir}/java/xmlgraphics-commons.jar:%{_datadir}/java/js.jar:%{_datadir}/java/sac.jar
javac --release 11 --add-modules jdk.xml.dom -encoding UTF-8 -cp "$cp" -d classes @sources.list
printf 'Class-Path: xml-apis-ext.jar xmlgraphics-commons.jar js.jar sac.jar\n' > manifest.mf
jar --create --file batik-all.jar --manifest manifest.mf -C classes .

%install
install -Dpm644 batik-all.jar %{buildroot}%{_datadir}/java/batik-all.jar

%check
# Run the upstream JUnit suites in the packaged CSS, bridge, Swing and utility modules.
# The legacy XML graphics harness additionally needs its external reference-image corpus.
mkdir classes-test
find batik-css batik-bridge batik-swing batik-util -path '*/src/test/java/*' -name '*.java' | sort > test.sources
find batik-test/src/main/java -name '*.java' ! -name 'MemoryLeakTest*' >> test.sources
cp=batik-all.jar:%{_datadir}/java/xml-apis-ext.jar:%{_datadir}/java/xmlgraphics-commons.jar:%{_datadir}/java/js.jar:%{_datadir}/java/sac.jar:%{_datadir}/java/junit4.jar
javac --release 11 --add-modules jdk.xml.dom -encoding UTF-8 -cp "$cp" -d classes-test @test.sources
for module in batik-css batik-bridge batik-swing batik-util batik-test; do
    if test -d "$module/src/test/resources"; then cp -rp "$module/src/test/resources/." classes-test/; fi
    if test -d "$module/src/main/resources"; then cp -rp "$module/src/main/resources/." classes-test/; fi
done
java -Djava.awt.headless=true -cp "classes-test:$cp" org.junit.runner.JUnitCore \
    org.apache.batik.css.parser.ParserTestCase \
    org.apache.batik.bridge.UserAgentAdapterTestCase \
    org.apache.batik.bridge.SVGUseElementBridgeTestCase \
    org.apache.batik.swing.svg.SVGUserAgentAdapterTestCase \
    org.apache.batik.util.UtilitiesTestSuite

%files
%license LICENSE NOTICE
%{_datadir}/java/batik-all.jar

%changelog
%autochangelog
