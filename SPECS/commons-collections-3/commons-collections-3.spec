# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           commons-collections-3
Version:        3.2.2
Release:        %autorelease
Summary:        Apache Commons Collections 3.x for Java
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-collections/
VCS:            git:https://github.com/apache/commons-collections.git
#!RemoteAsset:  sha256:070d94fe77969d8949bd129a618e6a7bee6b83b5b5db3ef3f983395a5428b914
Source0:        https://archive.apache.org/dist/commons/collections/source/commons-collections-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4
BuildRequires:  java-17-openjdk-devel

%description
The 3.x library supplies maps, collections, iterators and decorators in the
org.apache.commons.collections namespace.

%prep
%autosetup -n commons-collections-%{version}-src

%build
mkdir classes
find src/java -name '*.java' | sort > sources.list
# Java 8 added Map.remove(Object,Object) with a different return type.
%{_prefix}/lib64/jvm/java-17-openjdk/bin/javac --release 7 -encoding UTF-8 -d classes @sources.list
jar --create --file commons-collections3.jar -C classes .

%install
install -Dpm644 commons-collections3.jar %{buildroot}%{_datadir}/java/commons-collections3.jar

%check
# Run upstream's Ant test selection against the packaged library and Java 7 API.
# build.xml excludes aggregate/abstract suites and tests of JDK collection implementations.
mkdir classes-test
find src/test -name '*.java' | sort > test.sources
cp=commons-collections3.jar:%{_datadir}/java/junit4.jar
%{_prefix}/lib64/jvm/java-17-openjdk/bin/javac --release 7 -encoding UTF-8 -cp "$cp" -d classes-test @test.sources
suites=$(find src/test -name 'Test*.java' ! -name 'TestAll*' ! -name 'TestAbstract*' ! -name 'TestArrayList.java' ! -name 'TestLinkedList.java' ! -name 'TestHashMap.java' ! -name 'TestTreeMap.java' ! -name 'TestTypedCollection.java' | sed 's|^src/test/||;s|/|.|g;s|[.]java$||')
for suite in $suites; do
    %{_prefix}/lib64/jvm/java-17-openjdk/bin/java -cp "classes-test:data/test:$cp" junit.textui.TestRunner "$suite" || exit 1
done

%files
%license LICENSE.txt NOTICE.txt
%{_datadir}/java/commons-collections3.jar

%changelog
%autochangelog
