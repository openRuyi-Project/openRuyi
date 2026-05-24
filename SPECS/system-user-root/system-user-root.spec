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

Provides:       group(root)
Provides:       group(shadow)
Provides:       group(users)
Provides:       user(root)
#!BuildIgnore: group(root)
#!BuildIgnore: user(root)

%description
This package keeps compatibility provides for setup-owned root account
and base group identity declarations.

%prep
%setup -q -c -T

%build

%install

%files
%defattr(-,root,root)

%changelog
%autochangelog
