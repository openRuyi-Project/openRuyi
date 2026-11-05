# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bsh_dir %{_datadir}/maven-repository/org/apache-extras/beanshell/bsh/%{version}
%define bsh_ant ant -nouserlib -Dant.build.javac.source=8 -Dant.build.javac.target=8 -Djunit.jar=%{_datadir}/java/junit4.jar -Dhamcrest.jar=%{_datadir}/java/hamcrest1.3/hamcrest-core.jar -Dexclude-bsf=bsh/util/BeanShellBSFEngine.java,TestBshBSF.java

Name:           beanshell
Version:        2.1.1
Release:        %autorelease
Summary:        Embeddable Java source interpreter
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://beanshell.github.io/
VCS:            git:https://github.com/beanshell/beanshell
#!RemoteAsset:  sha256:12dada19d9554e3133d51f809e67d604e400b4c81ac70149db502de873741ec3
Source0:        https://github.com/beanshell/beanshell/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-hamcrest-1.3
BuildRequires:  javacc
BuildRequires:  javax-servlet-api
BuildRequires:  junit4
Provides:       mvn(org.apache-extras.beanshell:bsh) == %{version}
Requires:       java-25-openjdk

%patchlist
# https://github.com/beanshell/beanshell/commit/4ed14a79a4a9e5de27c2bc0a29d95d1fae86f28d
1000-report-filtered-junit-methods.patch
# https://github.com/beanshell/beanshell/commit/b01a7aff570ace1c66eef03133efc30ad67086f1
1001-import-script-engine-factory-in-test.patch
# https://github.com/beanshell/beanshell/commit/ca6d368aeef66908e4e9550ed93f23d896d07304
1002-recognize-binary-number-literals.patch
# https://github.com/beanshell/beanshell/commit/3afe1c973b012bc78754fbad0e7f7c9e36a82ef4
1003-select-exported-java-methods.patch
# https://github.com/beanshell/beanshell/commit/fa7c10c341de6c9cb22c780a209737bcb76adccd
1004-restore-class-static-initializers.patch
# https://github.com/beanshell/beanshell/commit/9a3f3e411bd7c651a3642a41cbfdb6687d24bc9f
1005-honor-nonpublic-member-declarations.patch
# https://github.com/beanshell/beanshell/commit/c98a9741cd3f2690c89927bfc60eb6849d71aae0
1006-apply-access-to-public-field-lookup.patch
# https://github.com/beanshell/beanshell/blob/2.1.1/build.xml
2000-select-ant-java-level.patch

%description
BeanShell evaluates Java expressions and scripts. Applications can embed
the interpreter through its Java API or the standard Java scripting
interface.

%prep
%autosetup -p1
cp -p src/bsh/org/objectweb/asm/LICENSE.txt LICENSE.asm
# Regenerate the lexer and parser from the patched grammar.
rm -f src/bsh/bsh.jj src/bsh/Parser.java src/bsh/JavaCharStream.java src/bsh/TokenMgrError.java
rm -f lib/*.jar
ln -s %{_datadir}/java/javacc.jar lib/javacc.jar
ln -s %{_datadir}/java/junit4.jar lib/junit.jar
ln -s %{_datadir}/java/hamcrest1.3/hamcrest-core.jar lib/hamcrest-core.jar
ln -s %{_datadir}/java/javax-servlet-api.jar lib/servlet.jar

%build
%{bsh_ant} jarall

%install
install -Dm644 dist/bsh-%{version}.jar %{buildroot}%{bsh_dir}/bsh-%{version}.jar
install -Dm644 pom.xml %{buildroot}%{bsh_dir}/bsh-%{version}.pom
install -d %{buildroot}%{_bindir} %{buildroot}%{_datadir}/maven-metadata %{buildroot}%{_datadir}/java
ln -s ../maven-repository/org/apache-extras/beanshell/bsh/%{version}/bsh-%{version}.jar %{buildroot}%{_datadir}/java/bsh.jar
cat > %{buildroot}%{_bindir}/bsh <<'EOF'
#!/bin/sh
exec java -cp %{bsh_dir}/bsh-%{version}.jar bsh.Interpreter "$@"
EOF
chmod 755 %{buildroot}%{_bindir}/bsh
cat > %{buildroot}%{_datadir}/maven-metadata/beanshell.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>org.apache-extras.beanshell</groupId><artifactId>bsh</artifactId><version>%{version}</version><path>%{bsh_dir}/bsh-%{version}.jar</path></artifact>
  <artifact><groupId>org.apache-extras.beanshell</groupId><artifactId>bsh</artifactId><extension>pom</extension><version>%{version}</version><path>%{bsh_dir}/bsh-%{version}.pom</path></artifact>
</artifacts></metadata>
EOF

%check
# Run the upstream JUnit classes in separate JVMs, as the Ant target does.
%{bsh_ant} -Dtest-build-dir=classes compile-tests build-junit-tests
# Java_9_Test requires external HTTPS. OldScriptsTest shares accessibility state
# between scripts and uses obsolete AWT/private-field and live-thread fixtures.
# Its aggregate cannot select individual scripts without changing the upstream runner.
suites=$(find tests/junitTests/src -name '*Test.java' ! -name Java_9_Test.java ! -name OldScriptsTest.java ! -name NumberLiteralTest.java ! -name Project_Coin_Test.java | sed 's|^tests/junitTests/src/||;s|/|.|g;s|[.]java$||')
cp=classes:%{_datadir}/java/junit4.jar:%{_datadir}/java/hamcrest1.3/hamcrest-core.jar:%{_datadir}/java/javax-servlet-api.jar
for suite in $suites; do
    java -ea -Dskip_known_issues=true -cp "$cp" org.junit.runner.JUnitCore "$suite" || exit 1
done
# The 2.1.1 grammar lacks BigInteger literals and try-with-resources. Keep the
# other methods in these classes through Ant's upstream method selector.
# https://github.com/beanshell/beanshell/commit/7f08518d25802279496c397b523f20a124636970
# https://github.com/beanshell/beanshell/commit/bff28804e1f4c048b9a3c330aff907f5394c61d5
cp="$cp:%{_datadir}/ant/lib/ant.jar:%{_datadir}/ant/lib/ant-junit.jar:%{_datadir}/ant/lib/ant-junit4.jar"
java -ea -Dskip_known_issues=true -cp "$cp" org.apache.tools.ant.taskdefs.optional.junit.JUnitTestRunner bsh.NumberLiteralTest methods=integer_literal_enhancements_hex,integer_literal_enhancements_octal,integer_literal_enhancements_binary,parsing_hex_literal,parse_long_hex_literal formatter=org.apache.tools.ant.taskdefs.optional.junit.PlainJUnitResultFormatter
java -ea -Dskip_known_issues=true -cp "$cp" org.apache.tools.ant.taskdefs.optional.junit.JUnitTestRunner bsh.Project_Coin_Test methods=integer_literal_enhancements,diamond_operator,try_with_resource_parsing,switch_on_strings formatter=org.apache.tools.ant.taskdefs.optional.junit.PlainJUnitResultFormatter

%files
%doc README.md
%license LICENSE NOTICE LICENSE.asm
%{_bindir}/bsh
%{_datadir}/java/bsh.jar
%{_datadir}/maven-metadata/beanshell.xml
%{bsh_dir}/

%changelog
%autochangelog
