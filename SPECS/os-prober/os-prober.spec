# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           os-prober
Version:        1.83
Release:        %autorelease
Summary:        Probes disks on the system for installed operating systems
License:        GPL-2.0-or-later
URL:            https://joeyh.name/code/os-prober/
VCS:            git:https://salsa.debian.org/installer-team/os-prober
#!RemoteAsset
Source0:        https://salsa.debian.org/installer-team/os-prober/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(build):  LDFLAGS="$LDFLAGS -fPIC"
BuildOption(build):  CFLAGS="$CFLAGS"
BuildOption(build):  CPPFLAGS="$CPPFLAGS"

BuildRequires:  make

Requires:       udev
Requires:       coreutils
Requires:       util-linux
Requires:       grep
Requires:       sed
Requires:       kmod

%description
This package detects other OSes available on a system and outputs the results
in a generic machine-readable format. Support for new OSes and Linux
distributions can be added easily.

%prep -a
find -type f -exec sed -i -e 's|usr/lib|usr/libexec|g' {} \;
# Change path of grub-mount and grub-probe to grub2-mount and grub2-probe
sed -i -e 's|grub-probe|grub2-probe|g' os-probes/common/50mounted-tests \
    linux-boot-probes/common/50mounted-tests
sed -i -e 's|grub-mount|grub2-mount|g' os-probes/common/50mounted-tests \
    linux-boot-probes/common/50mounted-tests common.sh

%conf
# No configure

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 -d %{buildroot}%{_localstatedir}/lib/%{name}

install -m 0755 -p os-prober linux-boot-prober %{buildroot}%{_bindir}
install -m 0755 -Dp newns %{buildroot}%{_libexecdir}/os-prober/newns
install -m 0644 -Dp common.sh %{buildroot}%{_datadir}/%{name}/common.sh

for probes in os-probes os-probes/mounted os-probes/init \
              linux-boot-probes linux-boot-probes/mounted; do
        install -m 755 -d %{buildroot}%{_libexecdir}/$probes
        cp -a $probes/common/* %{buildroot}%{_libexecdir}/$probes
        if [ -e "$probes/$ARCH" ]; then
                cp -a $probes/$ARCH/* %{buildroot}%{_libexecdir}/$probes
        fi
done

# no tests.
%check


%files
%doc README TODO debian/changelog
%license debian/copyright
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/%{name}
%{_localstatedir}/lib/%{name}

%changelog
%autochangelog
