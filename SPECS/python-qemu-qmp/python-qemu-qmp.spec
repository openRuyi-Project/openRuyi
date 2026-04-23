# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0
%bcond tests 0

%global srcname qemu-qmp
%global pypi_name qemu.qmp

Name:           python-%{srcname}
Version:        0.0.5
Release:        %autorelease
Summary:        QEMU Monitor Protocol library
License:        GPL-2.0-only AND LGPL-2.0-or-later
URL:            https://pypi.org/project/qemu.qmp
#!RemoteAsset:  sha256:1d1b9a9a5d57edfe2de3a1d888612823b09aff946951a902e79e9655a2aabbfd
Source:         https://files.pythonhosted.org/packages/source/q/%{pypi_name}/qemu_qmp-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l qemu

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif
%if %{with doc}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%endif

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
qemu.qmp is a QEMU Monitor Protocol ("QMP") library written in Python,
using asyncio. It is used to send QMP messages to running QEMU emulators.

%if %{with doc}
%package        doc
Summary:        Documentation for %{name}
%description    doc
This package provides offline HTML documentation for python3-qemu-qmp.
%endif

%generate_buildrequires
%pyproject_buildrequires

%install -a
rm -f %{buildroot}%{_bindir}/qmp-tui

%if %{with doc}
PYTHONPATH=${PWD} sphinx-build-3 docs html
PYTHONPATH=${PWD} sphinx-build-3 -b man docs man
rm -rf html/.{doctrees,buildinfo}
install -Dpm 0644 man/*.1 -t %{buildroot}%{_mandir}/man1/
%endif

%check
%if %{with tests}
%pyproject_check_import -e qemu.qmp.qmp_tui
%pytest -v
%endif

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE LICENSE_GPL2
%{_bindir}/qmp-shell
%{_bindir}/qmp-shell-wrap
%if %{with doc}
%{_mandir}/man1/qmp-shell.1*
%{_mandir}/man1/qmp-shell-wrap.1*
%endif

%if %{with doc}
%files doc
%doc html
%license LICENSE LICENSE_GPL2
%endif

%changelog
%autochangelog
