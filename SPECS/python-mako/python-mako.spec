# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mako

Name:           python-%{srcname}
Version:        1.3.12
Release:        %autorelease
Summary:        Mako template library for Python
License:        MIT AND Python-2.0.1 AND BSD-3-Clause
URL:            https://www.makotemplates.org/
#!RemoteAsset:  sha256:9f778e93289bd410bb35daadeb4fc66d95a746f0b75777b942088b7fd7af550a
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(markupsafe)
BuildRequires:  python3dist(lingua)
# For tests
BuildRequires:  python3dist(babel)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       python3dist(six)
Requires:       python3dist(lingua)

%description
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics.

%prep -a
# the package ends up installed as %%{version}.dev0 otherwise:
sed -i '/tag_build = dev/d' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%install -a
mv %{buildroot}/%{_bindir}/mako-render %{buildroot}/%{_bindir}/mako-render-%{python3_version}
ln -s ./mako-render-%{python3_version} %{buildroot}/%{_bindir}/mako-render-3
ln -s ./mako-render-%{python3_version} %{buildroot}/%{_bindir}/mako-render

%files -f %{pyproject_files}
%doc CHANGES README.rst examples
%license LICENSE
%{_bindir}/mako-render
%{_bindir}/mako-render-3
%{_bindir}/mako-render-%{python3_version}

%changelog
%autochangelog
