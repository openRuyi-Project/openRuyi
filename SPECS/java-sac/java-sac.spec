# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           java-sac
Version:        1.3
Release:        %autorelease
Summary:        Simple API for CSS parsers
License:        W3C-19980720
URL:            https://www.w3.org/Style/CSS/SAC/
# VCS: No VCS link available
#!RemoteAsset:  sha256:a228cae0e4c0cbefc7087cd1e17c0e8f91ee648949c6f0b9854c22f7ad1557b6
Source0:        https://www.w3.org/2002/06/sacjava-%{version}.zip
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip

%description
SAC defines the Java interfaces for CSS parsers, selectors, lexical units and parse events.

%prep
%autosetup -N -n sac-%{version}
# Rebuild the API from the W3C sources.
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete

%build
mkdir -p classes build/lib
find org -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
jar --create --file build/lib/sac.jar -C classes .

%install
install -Dpm644 build/lib/sac.jar %{buildroot}%{_datadir}/java/sac.jar

# The upstream source distribution does not include an automated test suite.

%files
%license COPYRIGHT.html
%{_datadir}/java/sac.jar

%changelog
%autochangelog
