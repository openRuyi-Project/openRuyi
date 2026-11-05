# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global lo_version 26.8.2.2

Name:           pentaho-flute
Version:        1.1.6
Release:        %autorelease
Summary:        CSS parser for Pentaho Reporting
License:        LGPL-2.1-only AND W3C-19980720
URL:            https://www.w3.org/Style/CSS/SAC/
VCS:            git:https://github.com/pentaho/pentaho-reporting.git
#!RemoteAsset:  sha256:1b5b24f7bc543c0362b667692f78db8bab4ed6dafc6172f104d0bd3757d8a133
Source0:        https://downloads.sourceforge.net/project/jfreereport/02.%20Libraries/%{version}-stable/flute-%{version}.zip
# The parser sources name LGPL version 2.1. The archive also contains the W3C notice.
#!RemoteAsset:  sha256:a190dc9c8043755d90f8b0a75fa66b9e42d4af4c980bf5ddc633f0124db3cee7
Source1:        https://raw.githubusercontent.com/pentaho/pentaho-reporting/3837c5c96af14ebe634c1d0870686d205de03d15/libraries/libpixie/licence-LGPL.txt
BuildArch:      noarch

# Upstream LibreOffice patches for this component.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/external/jfreereport/UnpackedTarball_jfreereport_flute.mk
#!RemoteAsset:  sha256:8980ba27dc14ba20a9f78ccf3c5612dbafdb7add66a95e75a0501bfddd82e765
Patch0:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/common_build.patch

BuildRequires:  ant
BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip
BuildRequires:  java-sac
Requires:       java-sac

%description
Flute parses CSS selectors, properties and style sheets using the W3C Simple API for CSS.

%prep
%autosetup -N -c
# Build all classes from source, including the dependencies used by Ant.
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete
sed -i 's/\r$//' common_build.xml
%patch -P 0 -p2
cp -p %{SOURCE1} COPYING.LGPL-2.1
mkdir -p lib
ln -s %{_datadir}/java/sac.jar lib/sac.jar

%build
ant -nouserlib -f build.xml -Dbuild.label=%{version} \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Dantcontrib.available=true -Dbuild.id=10682 -Dproject.revision=%{version} jar

%install
install -Dpm644 dist/flute-%{version}.jar %{buildroot}%{_datadir}/java/flute.jar

# The upstream source distribution does not include an automated test suite.

%files
%doc README.txt
%license COPYRIGHT.html COPYING.LGPL-2.1
%{_datadir}/java/flute.jar

%changelog
%autochangelog
