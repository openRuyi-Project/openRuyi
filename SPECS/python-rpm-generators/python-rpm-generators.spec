# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           python-rpm-generators
Version:        14
Release:        %autorelease
Summary:        Dependency generators for Python RPMs
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND (LicenseRef-openRuyi-Public-Domain OR LGPL-2.1-or-later OR GPL-2.0-or-later)
# I know...
URL:            https://src.fedoraproject.org/rpms/python-rpm-generators
Source0:        COPYING
Source1:        python.attr
Source2:        pythondist.attr
Source3:        pythonname.attr
Source4:        pythondistdeps.py
Source5:        pythonbundles.py
BuildArch:      noarch

%description
%{summary}.

%package     -n python3-rpm-generators
Summary:        %{summary}
Requires:       python3dist(packaging)
Requires:       rpm
Requires:       python-srpm-macros

%description -n python3-rpm-generators
%{summary}.

%prep
%autosetup -c -T
cp -a %{sources} .

%install
install -Dpm0644 -t %{buildroot}%{_fileattrsdir} *.attr
install -Dpm0755 -t %{buildroot}%{_rpmconfigdir} *.py

%files -n python3-rpm-generators
%license COPYING
%{_fileattrsdir}/python.attr
%{_fileattrsdir}/pythondist.attr
%{_fileattrsdir}/pythonname.attr
%{_rpmconfigdir}/pythondistdeps.py
%{_rpmconfigdir}/pythonbundles.py

%changelog
%autochangelog
