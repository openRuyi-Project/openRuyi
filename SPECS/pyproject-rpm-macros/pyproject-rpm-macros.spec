# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pyproject-rpm-macros
Version:        1.18.3
Release:        %autorelease
Summary:        RPM macros for PEP 517 Python packages
License:        MIT
# I know...
URL:            https://src.fedoraproject.org/rpms/pyproject-rpm-macros
# Macro files
Source0:        macros.pyproject
Source1:        macros.aaa-pyproject-srpm
# Implementation files
Source2:        pyproject_buildrequires.py
Source3:        pyproject_save_files.py
Source4:        pyproject_convert.py
Source5:        pyproject_preprocess_record.py
Source6:        pyproject_construct_toxenv.py
Source7:        pyproject_requirements_txt.py
Source8:        pyproject_wheel.py
Source9:        LICENSE
BuildArch:      noarch

BuildRequires:  rpm-build >= 4.14.90
BuildRequires:  python-rpm-macros
BuildRequires:  python-srpm-macros
BuildRequires:  python3-rpm-macros
Requires:       python-rpm-macros
Requires:       python-srpm-macros
Requires:       python3-rpm-macros

Requires:       /usr/bin/find
Requires:       /usr/bin/sed


%description
These macros allow projects that follow the Python packaging specifications
to be packaged as RPMs.

They work for:

* traditional Setuptools-based projects that use the setup.py file,
* newer Setuptools-based projects that have a setup.cfg file,
* general Python projects that use the PEP 517 pyproject.toml file
  (which allows using any build system, such as setuptools, flit or poetry).

These macros replace %%py3_build and %%py3_install,
which only work with setup.py.

%package     -n pyproject-srpm-macros
Summary:        Minimal implementation of %%pyproject_buildrequires
Requires:       pyproject-rpm-macros = %{version}-%{release}
Requires:       (rpm-build >= 4.14.90 if rpm-build)

%description -n pyproject-srpm-macros
This package contains a minimal implementation of %%pyproject_buildrequires.
When used in %%generate_buildrequires, it will generate BuildRequires
for pyproject-rpm-macros. When both packages are installed, the full version
takes precedence.

%prep
# Not strictly necessary but allows working on file names instead
# of source numbers in install section
%setup -c -T
cp -p %{sources} .

%generate_buildrequires
# Nothing to do

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmconfigdir}/openruyi
install -pm 644 macros.pyproject %{buildroot}%{_rpmmacrodir}/
install -pm 644 macros.aaa-pyproject-srpm %{buildroot}%{_rpmmacrodir}/
install -pm 644 pyproject_buildrequires.py %{buildroot}%{_rpmconfigdir}/openruyi/
install -pm 644 pyproject_convert.py %{buildroot}%{_rpmconfigdir}/openruyi/
install -pm 644 pyproject_save_files.py  %{buildroot}%{_rpmconfigdir}/openruyi/
install -pm 644 pyproject_preprocess_record.py %{buildroot}%{_rpmconfigdir}/openruyi/
install -pm 644 pyproject_construct_toxenv.py %{buildroot}%{_rpmconfigdir}/openruyi/
install -pm 644 pyproject_requirements_txt.py %{buildroot}%{_rpmconfigdir}/openruyi/
install -pm 644 pyproject_wheel.py %{buildroot}%{_rpmconfigdir}/openruyi/

%files
%license LICENSE
%{_rpmmacrodir}/macros.pyproject
%{_rpmconfigdir}/openruyi/pyproject_buildrequires.py
%{_rpmconfigdir}/openruyi/pyproject_convert.py
%{_rpmconfigdir}/openruyi/pyproject_save_files.py
%{_rpmconfigdir}/openruyi/pyproject_preprocess_record.py
%{_rpmconfigdir}/openruyi/pyproject_construct_toxenv.py
%{_rpmconfigdir}/openruyi/pyproject_requirements_txt.py
%{_rpmconfigdir}/openruyi/pyproject_wheel.py

%files -n pyproject-srpm-macros
%license LICENSE
%{_rpmmacrodir}/macros.aaa-pyproject-srpm

%changelog
%autochangelog
