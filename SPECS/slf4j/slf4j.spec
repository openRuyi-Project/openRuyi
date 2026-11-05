# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           slf4j
Version:        1.7.36
Release:        %autorelease
Summary:        Logging API for Java applications
License:        MIT
URL:            https://www.slf4j.org/
VCS:            git:https://github.com/qos-ch/slf4j
#!RemoteAsset:  sha256:a2deaffa191c81abbf830d4060eb84129f31b9b3b945b7791344e8875b595286
Source0:        https://github.com/qos-ch/slf4j/archive/refs/tags/v_%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4
Provides:       mvn(org.slf4j:slf4j-api) == %{version}

%description
SLF4J supplies a common logging API for Java applications. A runtime
binding determines where log messages are delivered.

%package        jdk14
Summary:        SLF4J binding for java.util.logging
Requires:       %{name} = %{version}-%{release}

%description    jdk14
The JDK binding delivers SLF4J messages to the Java runtime's logging system.

%package        jcl
Summary:        Commons Logging bridge to SLF4J
License:        MIT AND Apache-2.0
Requires:       %{name} = %{version}-%{release}

%description    jcl
This bridge implements the Commons Logging API and routes its calls to SLF4J.

%prep
%autosetup -n slf4j-v_%{version}

%build
for mod in slf4j-api slf4j-jdk14 jcl-over-slf4j; do
    src=$mod/src/main
    out=$mod/target/classes
    mkdir -p "$out"
    find "$src/java" -name '*.java' | sort > "$mod/target/sources"
    javac --release 8 -encoding UTF-8 -cp slf4j-api/target/classes -d "$out" @"$mod/target/sources"
    cp -rp "$src/resources/." "$out/"
    if test "$mod" = slf4j-api; then
        # The API compiles against temporary binding stubs that the release omits.
        rm -f "$out"/org/slf4j/impl/*.class
    fi
    manifest=$(sed -e 's/[$]{parsedVersion.osgiVersion}/%{version}/g' \
        -e 's/[$]{slf4j.api.minimum.compatible.version}/1.6.0/g' \
        "$out/META-INF/MANIFEST.MF")
    # The JUL manifest has no final newline; terminate its last field before appending.
    printf '%s\n' "$manifest" > "$mod/target/manifest"
    rm "$out/META-INF/MANIFEST.MF"
    if test "$mod" != slf4j-api; then
        printf 'Class-Path: slf4j-api.jar\n' >> "$mod/target/manifest"
    fi
    jar --create --file "$mod.jar" --manifest "$mod/target/manifest" -C "$out" .
done

%install
jars=%{buildroot}%{_datadir}/java
install -d "$jars"
install -pm644 slf4j-api.jar slf4j-jdk14.jar jcl-over-slf4j.jar "$jars/"
repo=%{_datadir}/maven-repository/org/slf4j/slf4j-api/%{version}
install -d "%{buildroot}$repo" %{buildroot}%{_datadir}/maven-metadata
ln -sr "$jars/slf4j-api.jar" "%{buildroot}$repo/slf4j-api-%{version}.jar"
install -pm644 slf4j-api/pom.xml "%{buildroot}$repo/slf4j-api-%{version}.pom"
cat > %{buildroot}%{_datadir}/maven-metadata/slf4j.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>org.slf4j</groupId><artifactId>slf4j-api</artifactId><version>%{version}</version><path>$repo/slf4j-api-%{version}.jar</path></artifact>
  <artifact><groupId>org.slf4j</groupId><artifactId>slf4j-api</artifactId><extension>pom</extension><version>%{version}</version><path>$repo/slf4j-api-%{version}.pom</path></artifact>
</artifacts></metadata>
EOF

%check
# Run the API no-binding suites. Aggregate suites duplicate these tests;
# MultithreadedInitializationTest is the abstract base of binding-specific tests.
mkdir -p api-tests
cp=slf4j-api.jar:%{_datadir}/java/junit4.jar:%{_datadir}/java/hamcrest1.3/hamcrest-core.jar
find slf4j-api/src/test/java -name '*.java' | sort > api-test.sources
javac --release 8 -encoding UTF-8 -cp "$cp" -d api-tests @api-test.sources
find api-tests -type f \( -name 'Test*.class' -o -name '*Test.class' -o -name '*Tests.class' -o -name '*TestCase.class' \) \
    ! -name '*$*' ! -name 'AllTest.class' ! -name 'PackageTest.class' ! -name 'MultithreadedInitializationTest.class' |
    sed 's|^api-tests/||;s|/|.|g;s|[.]class$||' | sort > suites.list
grep -Fx org.slf4j.NoBindingTest suites.list
while read -r suite; do java -cp "api-tests:$cp" org.junit.runner.JUnitCore "$suite" || exit 1; done < suites.list
# Run the upstream JUL binding and Commons Logging bridge suites separately.
for module in slf4j-jdk14 jcl-over-slf4j; do
    mkdir -p "$module/target/test-classes"
    find "$module/src/test/java" -name '*.java' | sort > "$module/target/test.sources"
    tc=slf4j-api.jar:slf4j-jdk14.jar:jcl-over-slf4j.jar:api-tests:%{_datadir}/java/junit4.jar
    javac --release 8 -encoding UTF-8 -cp "$tc" -d "$module/target/test-classes" @"$module/target/test.sources"
    suites=$(find "$module/src/test/java" -name '*Test.java' | sed "s|^$module/src/test/java/||;s|/|.|g;s|[.]java$||")
    for suite in $suites; do
        java -cp "$module/target/test-classes:$tc" org.junit.runner.JUnitCore "$suite" || exit 1
    done
done

%files
%doc README.md
%license LICENSE.txt
%{_datadir}/java/slf4j-api.jar
%{_datadir}/maven-repository/org/slf4j/slf4j-api/
%{_datadir}/maven-metadata/slf4j.xml

%files jdk14
%{_datadir}/java/slf4j-jdk14.jar

%files jcl
%license jcl-over-slf4j/LICENSE.txt
%{_datadir}/java/jcl-over-slf4j.jar

%changelog
%autochangelog
