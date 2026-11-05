# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

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
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit-3
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
# Test the packaged core and library matchers with upstream's JUnit 3 suites.
# Generator/integration suites belong to the modules not built by this package.
mkdir classes-test
find hamcrest-unit-test/src/main/java/org/hamcrest -name '*.java' ! -path '*/generator/*' ! -path '*/integration/*' | sort > test.sources
cp=hamcrest-core.jar:hamcrest-library.jar:%{_datadir}/java/junit-3.jar
javac --release 8 -encoding UTF-8 -cp "$cp" -d classes-test @test.sources
suites=$(find hamcrest-unit-test/src/main/java/org/hamcrest -name '*Test.java' ! -name 'Abstract*' ! -path '*/generator/*' ! -path '*/integration/*' | sed 's|^hamcrest-unit-test/src/main/java/||;s|/|.|g;s|[.]java$||')
for suite in $suites; do java -cp "classes-test:$cp" junit.textui.TestRunner "$suite" || exit 1; done

%files
%license LICENSE.txt
%{_datadir}/java/hamcrest%{version}/

%changelog
%autochangelog
