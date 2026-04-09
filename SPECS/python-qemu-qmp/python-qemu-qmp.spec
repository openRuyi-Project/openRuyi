# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0
%bcond tests 0

Name:           python-qemu-qmp
Version:        0.0.5
Release:        %autorelease
Summary:        QEMU Monitor Protocol library
License:        GPL-2.0-only AND LGPL-2.0-or-later
URL:            https://pypi.org/project/qemu.qmp
#!RemoteAsset
Source:         https://files.pythonhosted.org/packages/82/53/a7668df6a6051ecf714b3831526a8a754a3dae9a5ddea3e4f99a09547234/qemu_qmp-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install): -l qemu

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel

%if %{with tests}
BuildRequires:  python3-pytest
%endif

%if %{with doc}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-rtd-theme
%endif

Provides:       python3-qemu-qmp = %{version}-%{release}
%python_provide python3-qemu-qmp

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
%license LICENSE LICENSE_GPL2
%doc README.rst
%{_bindir}/qmp-shell
%{_bindir}/qmp-shell-wrap
%if %{with doc}
%{_mandir}/man1/qmp-shell.1*
%{_mandir}/man1/qmp-shell-wrap.1*
%endif

%if %{with doc}
%files doc
%license LICENSE LICENSE_GPL2
%doc html
%endif

%changelog
%autochangelog
