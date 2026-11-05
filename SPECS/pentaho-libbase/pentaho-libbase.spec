# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global lo_version 26.8.2.2

Name:           pentaho-libbase
Version:        1.1.6
Release:        %autorelease
Summary:        Base services for Pentaho Reporting
License:        LGPL-2.1-only
URL:            https://github.com/pentaho/pentaho-reporting
#!RemoteAsset:  sha256:75c80359c9ce343c20aab8a36a45cb3b9ee7c61cf92c13ae45399d854423a9ba
Source0:        https://downloads.sourceforge.net/project/jfreereport/02.%20Libraries/%{version}-stable/libbase-%{version}.zip
BuildArch:      noarch

# Upstream LibreOffice patches for this component.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/external/jfreereport/UnpackedTarball_jfreereport_libbase.mk
#!RemoteAsset:  sha256:8980ba27dc14ba20a9f78ccf3c5612dbafdb7add66a95e75a0501bfddd82e765
Patch0:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/common_build.patch
#!RemoteAsset:  sha256:643799262ba8aabe5f5cfc2072ef86e37e88883905e23d6c81ffbe15bf325306
Patch1:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/libbase-1.1.6-deprecated.patch
#!RemoteAsset:  sha256:99d23e3605ce8cf128b81ea340392b413d9a324599104432a99e4dc74fee9eae
Patch2:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/libbase-1.1.3-remove-commons-logging.patch.1

BuildRequires:  ant
BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip
BuildRequires:  junit4

%description
LibBase supplies configuration, module loading and utility classes for the Pentaho Reporting libraries.

%prep
%autosetup -N -c
# Build all classes from source, including the dependencies used by Ant.
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete
sed -i 's/\r$//' common_build.xml
%patch -P 0 -p2
%patch -P 1 -p2
%patch -P 2 -p1

%build
ant -nouserlib -f build.xml -Dbuild.label=%{version} \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Dantcontrib.available=true -Dbuild.id=10682 -Dproject.revision=%{version} jar

%install
install -Dpm644 dist/libbase-%{version}.jar %{buildroot}%{_datadir}/java/libbase.jar

%check
# Run the upstream JUnit regression suites with deterministic locale and time zone.
mkdir classes-test
find testcases -name '*.java' | sort > test.sources
javac --release 8 -encoding UTF-8 -cp dist/libbase-%{version}.jar:%{_datadir}/java/junit4.jar -d classes-test @test.sources
classes=$(while read -r file; do
    if grep -Eq 'public[[:space:]]+class[[:space:]]+' "$file" && grep -Eq 'public[[:space:]]+void[[:space:]]+test' "$file"; then
        echo "$file"
    fi
done < test.sources | sed -e 's|^testcases/||' -e 's|/|.|g' -e 's/[.]java$//')
test -n "$classes"
java -Djava.awt.headless=true -Duser.language=en -Duser.country=US -Duser.timezone=UTC \
    -cp classes-test:dist/libbase-%{version}.jar:%{_datadir}/java/junit4.jar org.junit.runner.JUnitCore $classes > upstream-tests.log
cat upstream-tests.log

%files
%doc README.txt
%license licence-LGPL.txt
%{_datadir}/java/libbase.jar

%changelog
%autochangelog
