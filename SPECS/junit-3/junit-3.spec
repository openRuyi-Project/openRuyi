# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           junit-3
Version:        3.8.2
Release:        %autorelease
Summary:        JUnit 3 test framework for legacy Java libraries
License:        CPL-1.0
URL:            https://junit.org/junit4/
VCS:            git:https://github.com/junit-team/junit4.git
#!RemoteAsset:  sha256:aae23d20e6f4dc45b4bf0b10fedcbd209c100342a0cafce1aa07d2da6da1f24a
Source0:        https://downloads.sourceforge.net/project/junit/junit/%{version}/junit%{version}.zip
BuildArch:      noarch

BuildRequires:  java-17-openjdk-devel
BuildRequires:  unzip

%description
JUnit 3 supplies the original Java unit-testing API and text runner.
It can test Hamcrest without the dependency on Hamcrest introduced by JUnit 4.

%prep
%autosetup -n junit%{version}
unzip -q src.jar
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete

%build
mkdir classes
find junit -name '*.java' ! -path 'junit/tests/*' ! -path 'junit/samples/*' | sort > sources.list
%{_prefix}/lib64/jvm/java-17-openjdk/bin/javac --release 7 -encoding ISO-8859-1 -d classes @sources.list
(cd junit && find . -type f ! -name '*.java' -exec cp --parents -p {} ../classes/junit/ \;)
%{_prefix}/lib64/jvm/java-17-openjdk/bin/jar --create --file junit-3.jar -C classes .

%install
install -Dpm644 junit-3.jar %{buildroot}%{_datadir}/java/junit-3.jar

%check
# Run the upstream framework, runner and extension aggregate suite.
mkdir classes-test
find junit/tests junit/samples -name '*.java' | sort > test.sources
%{_prefix}/lib64/jvm/java-17-openjdk/bin/javac --release 7 -encoding ISO-8859-1 -cp junit-3.jar -d classes-test @test.sources
%{_prefix}/lib64/jvm/java-17-openjdk/bin/java -Djava.awt.headless=true -cp classes-test:junit-3.jar junit.textui.TestRunner junit.tests.AllTests

%files
%license cpl-v10.html
%doc README.html
%{_datadir}/java/junit-3.jar

%changelog
%autochangelog
