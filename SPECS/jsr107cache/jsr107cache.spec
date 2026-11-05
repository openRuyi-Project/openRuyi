# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jsr107cache
Version:        1.0
Release:        %autorelease
Summary:        Original JSR 107 caching interfaces for Java
License:        Apache-2.0
URL:            https://sourceforge.net/projects/jsr107cache/
VCS:            svn:https://svn.code.sf.net/p/jsr107cache/code/
#!RemoteAsset:  sha256:c532eb77eefb528a70ac8faa42345261cc4a2fc0c4ebffeef308320af950e3e8
Source0:        https://downloads.sourceforge.net/project/jsr107cache/%{name}/%{name}-%{version}/%{name}-%{version}-bundle.jar
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip

%description
This version of the JCache API provides cache, loader, listener and statistics
interfaces in the net.sf.jsr107cache namespace.

%prep
%setup -q -c -T
unzip -q %{SOURCE0} LICENSE.txt %{name}-%{version}-sources.jar
unzip -q %{name}-%{version}-sources.jar

%build
mkdir classes
find net -name '*.java' | sort > sources.list
javac --release 8 -d classes @sources.list
jar --create --file jsr107cache.jar -C classes .

%install
install -Dpm644 jsr107cache.jar %{buildroot}%{_datadir}/java/jsr107cache.jar

# The upstream source distribution does not include an automated test suite.

%files
%license LICENSE.txt
%{_datadir}/java/jsr107cache.jar

%changelog
%autochangelog
