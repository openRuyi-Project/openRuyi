# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyudev

Name:           python-%{srcname}
Version:        0.24.3
Release:        %autorelease
Summary:        A libudev binding
License:        LGPL-2.1-or-later
URL:            https://pypi.python.org/pypi/pyudev
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset:  sha256:2e945427a21674893bb97632401db62139d91cea1ee96137cc7b07ad22198fc7
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

# Needed for libudev, loaded through ctypes
Requires:       systemd-libs

%description
pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.
The binding supports CPython 3 and PyPy.

%generate_buildrequires
%pyproject_buildrequires

# Do not run the declarative default import smoke test
# Because we exclude some modules
%check

%files -f %{pyproject_files}
%license COPYING
%doc README.rst
%exclude %{python3_sitelib}/pyudev/glib.py
%exclude %{python3_sitelib}/pyudev/__pycache__/glib.*
%exclude %{python3_sitelib}/pyudev/pyqt4.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyqt4.*
%exclude %{python3_sitelib}/pyudev/pyqt5.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyqt5.*
%exclude %{python3_sitelib}/pyudev/pyside.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyside.*
%exclude %{python3_sitelib}/pyudev/wx.py
%exclude %{python3_sitelib}/pyudev/__pycache__/wx.*

%changelog
%autochangelog
