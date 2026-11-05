# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global junit_version 4.13.2

Name:           java-hamcrest-1.3
Version:        1.3
Release:        %autorelease
Summary:        Hamcrest matchers for the original JUnit 4 API
License:        BSD-3-Clause
URL:            https://hamcrest.org/JavaHamcrest/
VCS:            git:https://github.com/hamcrest/JavaHamcrest
# The original release archive contains both the tagged source tree and the
# published source JARs with the two generated matcher factories.
#!RemoteAsset:  sha256:8e9ac0c51762cf8117df610740157749d1dfdffd9d4e6727e5af9056675e065f
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/hamcrest/hamcrest-%{version}.zip
# JUnit needs Hamcrest itself; build its test runner against the new matcher JARs.
#!RemoteAsset:  sha256:1b6d700fc374c82951d247f6d80238951d87c61661ceb151f9fbf40f65413561
Source1:        https://github.com/junit-team/junit4/archive/refs/tags/r%{junit_version}.tar.gz#/junit4-r%{junit_version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  java-17-openjdk-devel
BuildRequires:  unzip

%patchlist
# Downstream javac type-inference fix for the original 1.3 matcher API.
# https://github.com/hamcrest/JavaHamcrest/tree/hamcrest-java-1.3
2000-specify-matcher-type-in-varargs-delegates.patch

%description
Hamcrest 1.3 provides composable Java matchers and the Factory annotation
used by JUnit 4. Its core and library JARs are installed together in a
versioned directory.

%prep
%autosetup -N -n hamcrest-%{version}
for type in hamcrest-core hamcrest-library; do
    find "$type/src/main/java" -name '*.java' -exec sed -i 's/\r$//' {} +
done
%autopatch -p1
unzip -p hamcrest-core-%{version}-sources.jar org/hamcrest/CoreMatchers.java > hamcrest-core/src/main/java/org/hamcrest/CoreMatchers.java
unzip -p hamcrest-library-%{version}-sources.jar org/hamcrest/Matchers.java > hamcrest-library/src/main/java/org/hamcrest/Matchers.java
# The release also ships compiled JARs. Only the Java sources above are used.
find . -type f \( -name '*.class' -o -name '*.jar' \) -delete

%build
mkdir -p classes/{core,library}
find hamcrest-core/src/main/java -name '*.java' | sort > core.sources
javac --release 8 -encoding UTF-8 -d classes/core @core.sources
jar --create --file hamcrest-core.jar -C classes/core .
find hamcrest-library/src/main/java -name '*.java' | sort > library.sources
javac --release 8 -encoding UTF-8 -cp hamcrest-core.jar -d classes/library @library.sources
jar --create --file hamcrest-library.jar -C classes/library .

%install
install -d %{buildroot}%{_datadir}/java/hamcrest%{version}
install -pm644 hamcrest-{core,library}.jar %{buildroot}%{_datadir}/java/hamcrest%{version}/

%check
# Build the upstream JUnit runner against this Hamcrest build to avoid a
# Hamcrest-test -> JUnit -> Hamcrest package dependency cycle.
mkdir junit-runner classes-test
tar -xf %{SOURCE1}
find junit4-r%{junit_version}/src/main/java -name '*.java' | sort > junit.sources
javac --release 8 -encoding UTF-8 -cp hamcrest-core.jar -d junit-runner @junit.sources
cp -rp junit4-r%{junit_version}/src/main/resources/. junit-runner/
# Generator and integration tests exercise modules not packaged here.
# JDK 7 language mode retains the inference rules used by the original generic tests.
find hamcrest-unit-test/src/main/java/org/hamcrest -name '*.java' ! -name JavaLangMatcherAssertTest.java ! -path '*/generator/*' ! -path '*/integration/*' | sort > test.sources
cp=hamcrest-core.jar:hamcrest-library.jar:junit-runner
%{_prefix}/lib64/jvm/java-17-openjdk/bin/javac --release 7 -encoding UTF-8 -cp "$cp" -d classes-test @test.sources
suites=$(find hamcrest-unit-test/src/main/java/org/hamcrest -name '*Test.java' ! -name 'Abstract*' ! -name JavaLangMatcherAssertTest.java ! -path '*/generator/*' ! -path '*/integration/*' | sed 's|^hamcrest-unit-test/src/main/java/||;s|/|.|g;s|[.]java$||')
java -cp "classes-test:$cp" org.junit.runner.JUnitCore $suites

%files
%license LICENSE.txt
%{_datadir}/java/hamcrest%{version}/

%changelog
%autochangelog
