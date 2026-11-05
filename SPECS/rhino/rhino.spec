# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rhino
Version:        1.7.15.1
Release:        %autorelease
Summary:        JavaScript engine for Java applications
License:        MPL-2.0 AND BSD-3-Clause AND MIT
URL:            https://rhino.github.io/
VCS:            git:https://github.com/mozilla/rhino
#!RemoteAsset:  sha256:65599965d82c0e60332601d511dacb0241e796cabfa5550c72bb80c4bf89e8ad
Source0:        https://github.com/mozilla/rhino/releases/download/Rhino1_7_15_1_Release/rhino-%{version}.zip
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip
Requires:       java-25-openjdk-headless

%description
Rhino evaluates JavaScript in Java applications, in a standalone shell and
through the Java scripting API.

%prep
%autosetup -n rhino%{version}
# The release contains distribution JARs alongside the sources.
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete

%build
mkdir -p classes engine/META-INF/services
find src -name '*.java' | sort > java.sources
javac --release 8 -encoding UTF-8 -d classes @java.sources
(cd src && find org -type f ! -name '*.java' -exec cp --parents -p {} ../classes/ \;)
mkdir -p classes/META-INF engine/org/mozilla/javascript
cp -p LICENSE.txt NOTICE.txt NOTICE-tools.txt classes/META-INF/
mv classes/org/mozilla/javascript/engine engine/org/mozilla/javascript/
cp -p src/META-INF/services/javax.script.ScriptEngineFactory engine/META-INF/services/
cp -p LICENSE.txt engine/META-INF/
cat > core.mf <<'EOF'
Main-Class: org.mozilla.javascript.tools.shell.Main
Implementation-Version: %{version}
Implementation-Title: Mozilla Rhino
Implementation-Vendor: Mozilla Foundation
Implementation-URL: https://rhino.github.io/
Automatic-Module-Name: org.mozilla.rhino
Bundle-ManifestVersion: 2
Bundle-SymbolicName: org.mozilla.rhino
Bundle-Version: %{version}
Export-Package: org.mozilla.javascript,org.mozilla.javascript.ast,org.mozilla.javascript.annotations
Import-Package: javax.lang.model,javax.script
EOF
cat > engine.mf <<'EOF'
Implementation-Version: %{version}
Implementation-Title: Mozilla Rhino ScriptEngine
Implementation-Vendor: Mozilla Foundation
Automatic-Module-Name: org.mozilla.rhino.engine
Class-Path: js.jar
EOF
jar --create --file js.jar --manifest core.mf -C classes .
jar --create --file rhino-engine.jar --manifest engine.mf -C engine .

%install
install -Dpm644 js.jar %{buildroot}%{_datadir}/java/js.jar
install -pm644 rhino-engine.jar %{buildroot}%{_datadir}/java/rhino-engine.jar
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/rhino <<'EOF'
#!/bin/sh
exec java -jar %{_datadir}/java/js.jar "$@"
EOF
chmod 755 %{buildroot}%{_bindir}/rhino

# The upstream source distribution does not include an automated test suite.

%files
%license LICENSE.txt NOTICE.txt NOTICE-tools.txt
%{_bindir}/rhino
%{_datadir}/java/js.jar
%{_datadir}/java/rhino-engine.jar

%changelog
%autochangelog
