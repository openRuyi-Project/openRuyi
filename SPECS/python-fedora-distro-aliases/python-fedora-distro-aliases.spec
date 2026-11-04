# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fedora-distro-aliases
%global pypi_name fedora_distro_aliases

Name:           python-%{srcname}
Version:        1.8
Release:        %autorelease
Summary:        Aliases for active Fedora releases
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/fedora-distro-aliases
#!RemoteAsset:  sha256:8e59bb968241dbdcf50ac909ead252cdda82e50a252f147aa391086b966b85fd
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{pypi_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:aaf135472f81c5b4a0dca9367e5bb5e9750032b5bebe5442b36e4c0a47430df3
Source1:        https://raw.githubusercontent.com/rpm-software-management/fedora-distro-aliases/a18408a905d4cbf813273f955dd1094f89c001d8/LICENSES/GPL-2.0-or-later.txt
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Query the versions and aliases of active Fedora releases for tools that
work with Fedora release metadata.

%prep -a
cp -p %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires

%check -a
# The sdist omits the Bodhi fixtures. Check the installed CLI without network access.
PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/resolve-fedora-aliases --help

%files -f %{pyproject_files}
%doc README.md
%license GPL-2.0-or-later.txt
%{_bindir}/resolve-fedora-aliases

%changelog
%autochangelog
