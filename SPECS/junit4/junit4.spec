# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           junit4
Version:        4.13.2
Release:        %autorelease
Summary:        JUnit 4 unit testing framework for Java
License:        EPL-1.0
URL:            https://junit.org/junit4/
VCS:            git:https://github.com/junit-team/junit4
#!RemoteAsset:  sha256:1b6d700fc374c82951d247f6d80238951d87c61661ceb151f9fbf40f65413561
Source0:        https://github.com/junit-team/junit4/archive/refs/tags/r%{version}.tar.gz#/junit4-r%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
# The upstream suite exercises SecurityManager and ThreadGroup behavior available on JDK 17.
BuildRequires:  java-17-openjdk-headless
BuildRequires:  java-hamcrest-1.3
Requires:       java-hamcrest-1.3

%description
JUnit 4 supplies annotations, assertions and runners for Java tests.
It also runs test suites written for the JUnit 3 API.

%prep
%autosetup -n junit4-r%{version}
rm -f lib/hamcrest-core-1.3.jar lib/hamcrest-core-1.3-sources.jar
# The tagged checkout retains the development suffix replaced by the release process.
sed -i 's/"%{version}-SNAPSHOT"/"%{version}"/' src/main/java/junit/runner/Version.java

%build
mkdir classes
find src/main/java -name '*.java' | sort > java.sources
%{_prefix}/lib64/jvm/java-25-openjdk/bin/javac --release 8 -encoding UTF-8 \
    -cp %{_datadir}/java/hamcrest1.3/hamcrest-core.jar -d classes @java.sources
cp -a src/main/resources/. classes/
cat > junit.mf <<'MANIFEST'
Manifest-Version: 1.0
Implementation-Title: JUnit
Implementation-Version: %{version}
Class-Path: hamcrest1.3/hamcrest-core.jar
Automatic-Module-Name: junit

MANIFEST
jar --create --file junit4.jar --manifest junit.mf -C classes .

%install
install -Dpm644 junit4.jar %{buildroot}%{_datadir}/java/junit4.jar

%check
# Run the upstream aggregate suite on JDK 17, which supports its SecurityManager tests.
cp=junit4.jar:%{_datadir}/java/hamcrest1.3/hamcrest-core.jar:%{_datadir}/java/hamcrest1.3/hamcrest-library.jar
mkdir test-classes
find src/test/java -name '*.java' | sort > test.sources
%{_prefix}/lib64/jvm/java-25-openjdk/bin/javac --release 8 -encoding UTF-8 -cp "$cp" -d test-classes @test.sources
if test -d src/test/resources; then cp -a src/test/resources/. test-classes/; fi
%{_prefix}/lib64/jvm/java-17-openjdk/bin/java -cp "test-classes:$cp" \
    org.junit.runner.JUnitCore org.junit.tests.AllTests > upstream-tests.log
cat upstream-tests.log

%files
%license LICENSE-junit.txt
%{_datadir}/java/junit4.jar

%changelog
%autochangelog
