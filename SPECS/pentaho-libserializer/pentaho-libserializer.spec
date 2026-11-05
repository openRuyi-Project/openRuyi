# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global lo_version 26.8.2.2

Name:           pentaho-libserializer
Version:        1.1.6
Release:        %autorelease
Summary:        Object serialization for Pentaho Reporting
License:        LGPL-2.1-only
URL:            https://github.com/pentaho/pentaho-reporting
#!RemoteAsset:  sha256:05640a1f6805b2b2d7e2cb9c50db9a5cb084e3c52ab1a71ce015239b4a1d4343
Source0:        https://downloads.sourceforge.net/project/jfreereport/02.%20Libraries/%{version}-stable/libserializer-%{version}.zip
BuildArch:      noarch

# Upstream LibreOffice patches for this component.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/external/jfreereport/UnpackedTarball_jfreereport_libserializer.mk
#!RemoteAsset:  sha256:8980ba27dc14ba20a9f78ccf3c5612dbafdb7add66a95e75a0501bfddd82e765
Patch0:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/common_build.patch
#!RemoteAsset:  sha256:62ac23034f5a58d2b0b730f901d43f1154318ffcf7db0e4cb257fc823be9d455
Patch1:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/libserializer-1.1.2-remove-commons-logging.patch.1

BuildRequires:  ant
BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip
BuildRequires:  pentaho-libbase
Requires:       pentaho-libbase

%description
LibSerializer serializes drawing objects and other values used by the Pentaho Reporting engine.

%prep
%autosetup -N -c
# Build all classes from source, including the dependencies used by Ant.
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete
sed -i 's/\r$//' common_build.xml
%patch -P 0 -p2
%patch -P 1 -p1
mkdir -p lib
ln -s %{_datadir}/java/libbase.jar lib/libbase.jar

%build
ant -nouserlib -f build.xml -Dbuild.label=%{version} \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Dantcontrib.available=true -Dbuild.id=10682 -Dproject.revision=%{version} jar

%install
install -Dpm644 dist/libserializer-%{version}.jar %{buildroot}%{_datadir}/java/libserializer.jar

# The upstream source distribution does not include an automated test suite.

%files
%doc README.txt
%license licence-LGPL.txt
%{_datadir}/java/libserializer.jar

%changelog
%autochangelog
