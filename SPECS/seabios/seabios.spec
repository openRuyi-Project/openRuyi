# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           seabios
Version:        1.17.0
Release:        %autorelease
Summary:        Legacy x86 BIOS firmware for QEMU
License:        LGPL-3.0-only AND BSD-3-Clause
URL:            https://seabios.org/
VCS:            git:https://github.com/coreboot/seabios.git
#!RemoteAsset:  sha256:cb708a548e4244c5021590a5e78ab6e331ded1750120b687039042994033a07c
Source0:        https://github.com/coreboot/seabios/archive/refs/tags/rel-%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExclusiveArch:  x86_64

BuildRequires:  acpica
BuildRequires:  python3

%description
SeaBIOS implements a legacy x86 BIOS for virtual machines. This package
provides the 256 KiB firmware used by QEMU to boot its PC machines,
including the libguestfs appliance.

%prep
%autosetup -p1 -n %{name}-rel-%{version}
echo '%{version}' > .version
cat > .config <<'EOF'
CONFIG_QEMU=y
CONFIG_ROM_SIZE=256
EOF

%build
%make_build PYTHON=python3 EXTRAVERSION=-openruyi-%{release} olddefconfig
%make_build PYTHON=python3 EXTRAVERSION=-openruyi-%{release}

%install
install -D -p -m 0644 out/bios.bin %{buildroot}%{_datadir}/seabios/bios-256k.bin

%files
%doc README
%license COPYING COPYING.LESSER src/jpeg.c src/sha256.c src/sha512.c
%{_datadir}/seabios/

%changelog
%autochangelog
