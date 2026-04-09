# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global src_version 1_3_10

Name:           python-mako
Version:        1.3.10
Release:        %autorelease
Summary:        Mako template library for Python
License:        MIT AND Python-2.0.1 AND BSD-3-Clause
URL:            https://www.makotemplates.org/
#!RemoteAsset
Source0:        https://github.com/sqlalchemy/mako/archive/rel_%{src_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-markupsafe
BuildRequires:  expat

%description
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics.

%package     -n python3-mako
Summary:     %{summary}
%python_provide python3-mako
Requires:    python3-six

%description -n python3-mako
This package contains the mako module built for use with python3

Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics.

%prep
%autosetup -p1 -n mako-rel_%(echo %{version} | sed "s/\./_/g")
# the package ends up installed as %%{version}.dev0 otherwise:
sed -i '/tag_build = dev/d' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
#rm -rf %{buildroot}
%pyproject_install
%pyproject_save_files mako

mv %{buildroot}/%{_bindir}/mako-render %{buildroot}/%{_bindir}/mako-render-%{python3_version}
ln -s ./mako-render-%{python3_version} %{buildroot}/%{_bindir}/mako-render-3
ln -s ./mako-render-%{python3_version} %{buildroot}/%{_bindir}/mako-render

%files -n python3-mako -f %{pyproject_files}
%license LICENSE
%doc CHANGES README.rst examples
%{_bindir}/mako-render
%{_bindir}/mako-render-3
%{_bindir}/mako-render-%{python3_version}

%changelog
%autochangelog
