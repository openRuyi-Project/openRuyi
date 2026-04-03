# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fastapi
%global pkgname fastapi

Name:           python-%{srcname}
Version:        0.135.3
Release:        %autorelease
Summary:        FastAPI framework, high performance, easy to learn, fast to code, ready for production
License:        MIT
URL:            https://github.com/fastapi/fastapi
#!RemoteAsset:  sha256:bd6d7caf1a2bdd8d676843cdcd2287729572a1ef524fc4d65c17ae002a1be654
Source0:        https://files.pythonhosted.org/packages/source/f/fastapi/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install):  -l %{pkgname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
FastAPI is a modern, fast (high-performance), web framework for building
APIs with Python based on standard Python type hints.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{pkgname}-%{version}

%check
exit 0

%files -f %{pyproject_files}
%{_bindir}/fastapi
%doc README.md
%license LICENSE

%changelog
%autochangelog
