# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-rpm-packaging
Version:        1.2
Release:        %autorelease
Summary:        RPM dependency generator for Perl
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/perl-rpm-packaging
#!RemoteAsset
Source0:        https://github.com/rpm-software-management/perl-rpm-packaging/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-fileattrs.diff
BuildArch:      noarch
Requires:       perl

%description
Tools for packaging Perl projects with rpm

%prep
%autosetup -p0

%install
mkdir -p %{buildroot}%{_fileattrsdir}
install -Dm0644 fileattrs/* %{buildroot}%{_fileattrsdir}
install -Dm0755 scripts/* %{buildroot}%{_rpmconfigdir}

%files
%doc README.md
%{_fileattrsdir}/perl.attr
%{_fileattrsdir}/perllib.attr
%{_rpmconfigdir}/perl.prov
%{_rpmconfigdir}/perl.req

%changelog
%autochangelog
