# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ant
Version:        1.10.18
Release:        %autorelease
Summary:        Java build tool
License:        Apache-2.0
URL:            https://ant.apache.org/
VCS:            git:https://github.com/apache/ant.git
#!RemoteAsset:  sha256:9c8b71ca430bc5135c4914d37c947ea6b8f044c81aae3adfffbe8fbac7b0e185
Source0:        https://archive.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.bz2
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  java-hamcrest-1.3
BuildRequires:  junit4
BuildRequires:  which
Requires:       java-25-openjdk-headless
Requires:       sed
Requires:       which

%description
Apache Ant runs XML build files and provides tasks for compiling Java
sources, running programs and producing distribution archives.

%package        junit
Summary:        JUnit 3 and JUnit 4 tasks for Apache Ant
Requires:       %{name} = %{version}-%{release}
Requires:       junit4

%description    junit
The optional JUnit tasks run Java test suites and write Ant XML test reports.

%prep
%autosetup -n apache-ant-%{version}
# dist-lite compiles the test sources and the JUnit adapters against lib/optional.
# Keep the signed-JAR fixtures in src/etc/testcases used to test archive signatures.
find lib -type f -name '*.jar' -delete
ln -s %{_datadir}/java/junit4.jar lib/optional/junit4.jar
ln -s %{_datadir}/java/hamcrest1.3/hamcrest-core.jar lib/optional/hamcrest-core.jar
ln -s %{_datadir}/java/hamcrest1.3/hamcrest-library.jar lib/optional/hamcrest-library.jar

%build
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f "$(command -v javac)")")")
sh build.sh -Ddist.dir="$PWD/dist" dist-lite

%install
home=%{buildroot}%{_datadir}/ant
install -d "$home"/{bin,lib} %{buildroot}%{_bindir}
install -pm755 dist/bin/{ant,antRun} "$home/bin/"
install -pm644 dist/lib/{ant,ant-launcher,ant-junit,ant-junit4}.jar "$home/lib/"
ln -s %{_datadir}/java/junit4.jar "$home/lib/junit4.jar"
ln -s %{_datadir}/java/hamcrest1.3/hamcrest-core.jar "$home/lib/hamcrest-core.jar"
# The upstream launcher follows its own symlink when invoked through /bin.
ln -s %{_datadir}/ant/bin/ant %{buildroot}%{_bindir}/ant

%check
# Run the upstream JUnit target with its offline detection and dependency exclusions.
# Fail immediately when an executed upstream test fails.
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f "$(command -v javac)")")")
sh build.sh -Ddist.dir="$PWD/dist" -Doffline=true -Dtest.haltonfailure=true junit-tests

%files
%doc README
%license LICENSE NOTICE
%{_bindir}/ant
%dir %{_datadir}/ant/
%{_datadir}/ant/bin/
%dir %{_datadir}/ant/lib/
%{_datadir}/ant/lib/ant.jar
%{_datadir}/ant/lib/ant-launcher.jar

%files junit
%{_datadir}/ant/lib/ant-junit.jar
%{_datadir}/ant/lib/ant-junit4.jar
%{_datadir}/ant/lib/junit4.jar
%{_datadir}/ant/lib/hamcrest-core.jar

%changelog
%autochangelog
