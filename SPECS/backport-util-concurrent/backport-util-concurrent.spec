# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           backport-util-concurrent
Version:        3.1
Release:        %autorelease
Summary:        Concurrency primitives for the Emory Java backport
License:        CC-PDDC
URL:            https://backport-jsr166.sourceforge.net/
# VCS: No VCS link available
#!RemoteAsset:  sha256:2e6ea2678e1efb8f0b3b149f35d10ae7454c46527a4dc1c84f6f3ababa38e4cd
Source0:        https://downloads.sourceforge.net/project/backport-jsr166/backport-jsr166/%{version}/%{name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4
# The upstream security-policy TCK requires APIs removed after JDK 17.
BuildRequires:  java-17-openjdk-headless

%description
The Emory backport provides the JSR-166 concurrency API in the namespace
used by older Java applications.

%prep
%autosetup -n %{name}-%{version}-src

%build
mkdir classes
find src/edu src/sun -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
# The sun.misc sources are compile-time stubs. Use the JDK's own classes at runtime.
jar --create --file backport-util-concurrent.jar -C classes edu

%install
install -Dpm644 backport-util-concurrent.jar %{buildroot}%{_datadir}/java/backport-util-concurrent.jar

%check
# Run the upstream JSR-166 TCK, including its concurrency timing allowance.
mkdir classes-test
find test/tck/src -name '*.java' | sort > test.sources
javac --release 8 -encoding UTF-8 -cp backport-util-concurrent.jar:%{_datadir}/java/junit4.jar -d classes-test @test.sources
# Match upstream's combined test JAR so access-control contexts share a code source.
jar --create --file backport-util-concurrent-test.jar -C classes edu -C classes-test .
%{_prefix}/lib64/jvm/java-17-openjdk/bin/java -Dtck.shortDelay=100 -cp backport-util-concurrent-test.jar:%{_datadir}/java/junit4.jar junit.textui.TestRunner JSR166TestCase

%files
%license license.html
%{_datadir}/java/backport-util-concurrent.jar

%changelog
%autochangelog
