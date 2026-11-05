# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           javacc
Version:        7.0.13
Release:        %autorelease
Summary:        Java parser generator and tree preprocessor
License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://javacc.github.io/javacc/
VCS:            git:https://github.com/javacc/javacc
#!RemoteAsset:  sha256:d1bfebb4ca9261c5c3b16b00280b3278a41b193ca8503f2987f72de453bf99c6
Source0:        https://github.com/javacc/javacc/archive/refs/tags/javacc-%{version}.tar.gz#/javacc-%{version}.tar.gz
BuildArch:      noarch

# Fedora's generated Java sources for the three upstream bootstrap grammars.
# https://github.com/fedora-java/javapackages-bootstrap/tree/f7f74e76145c0dc4ea4d0d1967ef678ffaa7cf87/patches/javacc
#!RemoteAsset:  sha256:683c9ebfe74053b5a077b32acff2674cc6fdcf8d18e820f8c6b5da514ab92647
Patch0:         https://raw.githubusercontent.com/fedora-java/javapackages-bootstrap/f7f74e76145c0dc4ea4d0d1967ef678ffaa7cf87/patches/javacc/0001-Generate-bootstrap-sources.patch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  ant
# The functional-test build files explicitly compile Java 7 source.
BuildRequires:  java-17-openjdk-devel
Requires:       java-25-openjdk-headless

%description
JavaCC generates Java parsers from grammar files. JJTree adds tree nodes
to a grammar and JJDoc produces grammar documentation.

%prep
%autosetup -n javacc-javacc-%{version} -p1
# The source archive carries a bootstrap compiler and binary build dependencies.
find bootstrap lib -type f -name '*.jar' -delete

%build
mkdir -p bootstrap-classes classes
find src/main/java generated -name '*.java' | sort > bootstrap.sources
javac --release 8 -encoding UTF-8 -d bootstrap-classes @bootstrap.sources
cp -rp src/main/resources/. bootstrap-classes/

# Regenerate the compiler and tree preprocessor from their upstream grammars.
generated=$PWD/regenerated/org/javacc
mkdir -p "$generated"/{parser,jjtree,utils}
java -cp bootstrap-classes javacc -OUTPUT_DIRECTORY="$generated/parser" src/main/javacc/JavaCC.jj
java -cp bootstrap-classes jjtree -OUTPUT_DIRECTORY="$generated/jjtree" src/main/jjtree/JJTree.jjt
java -cp bootstrap-classes javacc -OUTPUT_DIRECTORY="$generated/jjtree" "$generated/jjtree/JJTree.jj"
java -cp bootstrap-classes javacc -OUTPUT_DIRECTORY="$generated/utils" src/main/javacc/ConditionParser.jj
# Keep authored implementations where the grammar also emits a default class.
find src/main/java -name '*.java' > sources.list
(cd regenerated && find . -name '*.java' | while read -r file; do
    test -f "../src/main/java/$file" || echo "regenerated/$file"
done) >> sources.list
sort -o sources.list sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
cp -rp src/main/resources/. classes/
jar --create --file javacc.jar -C classes .

%install
install -Dpm644 javacc.jar %{buildroot}%{_datadir}/java/javacc.jar
install -d %{buildroot}%{_bindir}
for command in javacc jjtree jjdoc; do
    printf '#!/bin/sh\nexec java -cp %{_datadir}/java/javacc.jar %%s "$@"\n' "$command" > %{buildroot}%{_bindir}/"$command"
    chmod 755 %{buildroot}%{_bindir}/"$command"
done

%check
# Run the upstream parser-generator functional regressions against the rebuilt JAR.
mkdir -p target
cp -p javacc.jar target/javacc.jar
JAVA_HOME=%{_prefix}/lib64/jvm/java-17-openjdk ant -nouserlib -f test/build.xml test

%files
%doc README.md
%license LICENSE
%{_bindir}/javacc
%{_bindir}/jjtree
%{_bindir}/jjdoc
%{_datadir}/java/javacc.jar

%changelog
%autochangelog
