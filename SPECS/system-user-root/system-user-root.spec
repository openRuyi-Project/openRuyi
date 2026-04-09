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

Provides:       group(root)
Provides:       group(shadow)
Provides:       group(trusted)
Provides:       group(users)
Provides:       user(root)
#!BuildIgnore: group(root)
#!BuildIgnore: group(trusted)
#!BuildIgnore: user(root)

%description
This package provides the root account including the groups root,
shadow and users.

%prep
%setup -q -c -T

%build

%install
mkdir -p %{buildroot}%{_libdir}/sysusers.d
install -m 644 %{SOURCE1} %{buildroot}%{_libdir}/sysusers.d/system-user-root.conf

%pre -p <lua>
if not posix.access("/etc", "f") then
  posix.mkdir("/etc")
end
if not posix.access("/etc/passwd", "f") then
  file = io.open("/etc/passwd", "a+")
  file:write("root:x:0:0:root:/root:/bin/bash\n")
  file:close()
  posix.chmod("/etc/passwd", 0644)
end
if not posix.access("/etc/group", "f") then
  file = io.open("/etc/group", "a+")
  file:write("root:x:0:\nshadow:x:15:\ntrusted:x:42:\nusers:x:100:\n")
  file:close()
  posix.chmod("/etc/group", 0644)
end
if not posix.access("/etc/shadow", "f") then
  file = io.open("/etc/shadow", "a+")
  local date = os.time()
  date = math.floor(date / 86400)
  file:write("root:*:", date, "::::::\n")
  file:close()
  posix.chown("/etc/shadow", 0, 15)
  posix.chmod("/etc/shadow", 0640)
end

%files
%defattr(-,root,root)
%{_libdir}/sysusers.d/system-user-root.conf

%changelog
%autochangelog
