# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>

%global srcname airportsdata

Name:           python-%{srcname}
Version:        20260905
Release:        %autorelease
Summary:        Extensive airport location and timezone database
License:        MIT
URL:            https://github.com/mborsetti/airportsdata
#!RemoteAsset:  sha256:a7e17469458ca356a5ca9971f49864b934a559d43e1587e19219cb981d364c45
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%prep
%autosetup -n %{srcname}-%{version}
sed -i '1{/^#!/d;}' airportsdata/__init__.py

%description
airportsdata provides extensive location and timezone data for operational
airports, landing strips, and selected seaplane bases worldwide.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
