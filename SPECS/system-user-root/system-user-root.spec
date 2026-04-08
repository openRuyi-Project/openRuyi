# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           system-user-root
Version:        20190513
Release:        %autorelease
Summary:        System user and group root
License:        MIT
Source1:        system-user-root.conf
BuildRequires:  systemd-rpm-macros
Requires(pre):  systemd-sysusers

Provides:       group(root)
Provides:       group(shadow)
Provides:       group(trusted)
Provides:       group(users)
Provides:       user(root)
#!BuildIgnore: group(root)
#!BuildIgnore: group(trusted)
#!BuildIgnore: user(root)

%description
This package keeps compatibility provides for the root account and
ensures the trusted group exists without duplicating setup-owned base
identity declarations.

%prep
%setup -q -c -T

%build

%install
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/system-user-root.conf

%pre
%sysusers_create_package %{name} %{SOURCE1}

%files
%defattr(-,root,root)
%{_sysusersdir}/system-user-root.conf

%changelog
%autochangelog
