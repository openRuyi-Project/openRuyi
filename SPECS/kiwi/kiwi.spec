# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# 75 failed, 1248 passed, 510 errors - 251
%bcond check 0
%bcond docs 0
%bcond containers 0
%bcond containers_wsl 0
# TODO: pxeboot is only for x86_64 for now
%bcond pxeboot 0

Name:           kiwi
Version:        10.2.42
Release:        %autorelease
Summary:        Flexible operating system image builder
License:        GPL-3.0-or-later
URL:            http://osinside.github.io/kiwi/
VCS:            git:https://github.com/OSInside/kiwi.git
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/k/%{name}/%{name}-%{version}.tar.gz

%if %{without docs}
Patch0:         2000-optional-manpage.patch
%endif

BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  dracut
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  shadow
# for docs
%if %{with docs}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%endif
# for tests
%if %{with check}
BuildRequires:  python3dist(pytest)
%endif

Requires:      %{name}-systemdeps = %{version}-%{release}
Requires:      python3dist(kiwi)

%description
KIWI is a powerful, command-line-driven tool that allows you to create
customized Linux operating system images for a variety of platforms and
use cases. Whether you're building for bare metal, virtual machines,
containers, or cloud environments, KIWI provides the flexibility and
control you need to craft the perfect OS image.

%package        systemdeps-bootloaders
Summary:        KIWI - host requirements for configuring bootloaders
Requires:       grub

%description    systemdeps-bootloaders
Host setup helper to pull in all packages required/useful on the
build host for configuring bootloaders on images.

%package        systemdeps-core
Summary:        KIWI - Core host system dependencies
Provides:       kiwi-image-tbz-requires = %{version}-%{release}
Obsoletes:      kiwi-image-tbz-requires < %{version}-%{release}
Provides:       kiwi-image:tbz
# We use dnf5 as the default package manager
Requires:       dnf5
Provides:       kiwi-packagemanager:dnf5
# Tools used by kiwi
Requires:       mtools
Requires:       rsync
Requires:       tar
Requires:       cpio
Requires:       lsof
Requires:       openssl
Requires:       xz

%description    systemdeps-core
This metapackage installs the necessary system dependencies to run KIWI.

%if %{with containers}
%package        systemdeps-containers
Summary:        KIWI - host requirements for container images
Provides:       kiwi-image:docker
Provides:       kiwi-image:oci
Provides:       kiwi-image-docker-requires = %{version}-%{release}
Obsoletes:      kiwi-image-docker-requires < %{version}-%{release}
Requires:       buildah
Requires:       skopeo
%if %{with containers_wsl}
Provides:       kiwi-image:appx
Provides:       kiwi-image:wsl
Provides:       kiwi-image-wsl-requires = %{version}-%{release}
Obsoletes:      kiwi-image-wsl-requires < %{version}-%{release}
Requires:       appx-util
%endif

%description    systemdeps-containers
Host setup helper to pull in all packages required/useful on the
build host to build container images.
%endif

%package        systemdeps-disk-images
Summary:        KIWI - host requirements for disk images
Provides:       kiwi-image:oem
Provides:       kiwi-image:vmx
Provides:       kiwi-image-oem-requires = %{version}-%{release}
Obsoletes:      kiwi-image-oem-requires < %{version}-%{release}
Provides:       kiwi-image-vmx-requires = %{version}-%{release}
Obsoletes:      kiwi-image-vmx-requires < %{version}-%{release}
Requires:       kiwi-systemdeps-filesystems = %{version}-%{release}
Requires:       kiwi-systemdeps-bootloaders = %{version}-%{release}
Requires:       kiwi-systemdeps-iso-media = %{version}-%{release}
Requires:       gptfdisk
Requires:       lvm2
Requires:       parted
Requires:       kpartx
Requires:       cryptsetup
Requires:       mdadm
Requires:       open-vmdk
Requires:       util-linux

%description    systemdeps-disk-images
Host setup helper to pull in all packages required/useful on the
build host to build disk images.

%package        systemdeps-filesystems
Summary:        KIWI - host requirements for filesystems
Provides:       kiwi-image:pxe
Provides:       kiwi-image:kis
Provides:       kiwi-image:erofs
Provides:       kiwi-filesystem:btrfs
Provides:       kiwi-filesystem:erofs
Provides:       kiwi-filesystem:ext2
Provides:       kiwi-filesystem:ext3
Provides:       kiwi-filesystem:ext4
Provides:       kiwi-filesystem:squashfs
Provides:       kiwi-filesystem:xfs
Provides:       kiwi-image-pxe-requires = %{version}-%{release}
Obsoletes:      kiwi-image-pxe-requires < %{version}-%{release}
Provides:       kiwi-filesystem-requires = %{version}-%{release}
Obsoletes:      kiwi-filesystem-requires < %{version}-%{release}
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       erofs-utils
Requires:       xfsprogs
Requires:       btrfs-progs
Requires:       squashfs-tools
Requires:       qemu-tools
Requires:       kiwi-systemdeps-core = %{version}-%{release}

%description    systemdeps-filesystems
Host setup helper to pull in all packages required/useful on the
build host to build filesystem images.

%package        systemdeps-iso-media
Summary:        KIWI - host requirements for live and install iso images
Provides:       kiwi-image:iso
Provides:       kiwi-image-iso-requires = %{version}-%{release}
Obsoletes:      kiwi-image-iso-requires < %{version}-%{release}
Requires:       kiwi-systemdeps-core = %{version}-%{release}
Requires:       kiwi-systemdeps-filesystems = %{version}-%{release}
Requires:       kiwi-systemdeps-bootloaders = %{version}-%{release}
Requires:       xorriso
Requires:       isomd5sum

%description    systemdeps-iso-media
Host setup helper to pull in all packages required/useful on the
build host to build live and install iso images.

%package        systemdeps-image-validation
Summary:        KIWI - host requirements for handling image descriptions better
Recommends:     jing
Requires:       python3dist(solv)

%description    systemdeps-image-validation
Host setup helper to pull in all packages required/useful on the
build host to handling image descriptions better. This also includes
reading of image descriptions for different markup languages.

%package        systemdeps
Summary:        KIWI - Host system dependencies
Requires:       kiwi-systemdeps-core = %{version}-%{release}
Requires:       kiwi-systemdeps-bootloaders = %{version}-%{release}
%if %{with containers}
Requires:       kiwi-systemdeps-containers = %{version}-%{release}
%endif
Requires:       kiwi-systemdeps-filesystems = %{version}-%{release}
Requires:       kiwi-systemdeps-disk-images = %{version}-%{release}
Requires:       kiwi-systemdeps-iso-media = %{version}-%{release}
Requires:       kiwi-systemdeps-image-validation = %{version}-%{release}

%description    systemdeps
Host setup helper to pull in all packages required/useful to leverage
all functionality in KIWI.

%package     -n python-%{name}
Summary:        KIWI - Python 3 implementation
BuildArch:      noarch
# Only require core dependencies, and allow OBS to pull the rest through magic Provides
Requires:       kiwi-systemdeps-core = %{version}-%{release}
# Retain default expectation for local installations
Recommends:     kiwi-systemdeps = %{version}-%{release}
Requires:       python3dist(lxml)
Requires:       python3dist(requests)
Requires:       python3dist(xmltodict)
Provides:       python3-kiwi = %{version}-%{release}
%python_provide python3-%{name}

%description -n python-%{name}
Python 3 library of the KIWI Image System. Provides an operating system
image builder for Linux supported hardware platforms as well as for
virtualization and cloud systems like Xen, KVM, VMware, EC2 and more.

%if %{with pxeboot}
%ifarch x86_64
%package        pxeboot
Summary:        KIWI - PXE boot structure
Requires:       syslinux

%description    pxeboot
This package contains the basic PXE directory structure which is needed
to serve kiwi built images via PXE.
%endif
%endif

%package     -n dracut-kiwi-lib
Summary:        KIWI - Dracut kiwi Library
BuildArch:      noarch
Requires:       bc
Requires:       btrfs-progs
Requires:       coreutils
Requires:       cryptsetup
Requires:       curl
Requires:       device-mapper
Requires:       dialog
Requires:       dracut
Requires:       e2fsprogs
Requires:       gptfdisk
Requires:       grep
Requires:       kpartx
Requires:       lvm2
Requires:       mdadm
Requires:       parted
Requires:       pv
Requires:       util-linux
Requires:       xfsprogs
Requires:       xz

%description -n dracut-kiwi-lib
This package contains a collection of methods to provide a library for
tasks done in other kiwi dracut modules.

%package     -n dracut-kiwi-live
Summary:        KIWI - Dracut module for iso(live) image type
Requires:       dracut-kiwi-lib = %{version}-%{release}
Requires:       device-mapper
Requires:       dialog
Requires:       dracut
Requires:       e2fsprogs
Requires:       util-linux
Requires:       xfsprogs
Requires:       parted
BuildArch:      noarch

%description -n dracut-kiwi-live
This package contains the kiwi-live dracut module which is used for
booting iso(live) images built with KIWI.

%package     -n dracut-kiwi-oem-dump
Summary:        KIWI - Dracut module for oem(install) image type
Requires:       dracut-kiwi-lib = %{version}-%{release}
Requires:       gawk
Requires:       kexec-tools
BuildArch:      noarch

%description -n dracut-kiwi-oem-dump
This package contains the kiwi-dump and kiwi-dump-reboot dracut modules
which is used to install an oem image onto a target disk.
It implements a simple installer which allows for user selected target
disk or unattended installation to target. The source of the image to
install could be either from media(CD/DVD/USB) or from remote.

%package     -n dracut-kiwi-oem-repart
Summary:        KIWI - Dracut module for oem(repart) image type
Requires:       dracut-kiwi-lib = %{version}-%{release}
BuildArch:      noarch

%description -n dracut-kiwi-oem-repart
This package contains the kiwi-repart dracut module which is used to
repartition the oem disk image to the current disk geometry according
to the setup in the kiwi image configuration.

%package     -n dracut-kiwi-overlay
Summary:        KIWI - Dracut module for vmx(+overlay) image type
Requires:       dracut-kiwi-lib = %{version}-%{release}
Requires:       dracut
Requires:       util-linux
BuildArch:      noarch

%description -n dracut-kiwi-overlay
This package contains the kiwi-overlay dracut module which is used for
booting vmx images built with KIWI and configured to use an overlay root
filesystem.

%package     -n dracut-kiwi-verity
Summary:        KIWI - Dracut module for disk with embedded verity metadata
Requires:       dracut-kiwi-lib = %{version}-%{release}
Requires:       dracut

%description -n dracut-kiwi-verity
This package contains the kiwi-verity dracut module which is used for
booting oem images built with KIWI and configured to use an embedded verity
metadata block via the embed_verity_metadata type attribute.

%prep
%autosetup -p1

# Drop shebang for kiwi/xml_parse.py, as we don't intend to use it as an independent script
sed -e "s|#!/usr/bin/env python||" -i kiwi/xml_parse.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with docs}
# Build docs
make -C doc man
%endif

%install
%pyproject_install

# DO NOT REMOVE THE SLASH HERE!
# man-pages, completion and kiwi default configuration
make buildroot=%{buildroot}/ install
# dracut modules
make buildroot=%{buildroot}/ install_dracut
# other docs
%if %{with docs}
make buildroot=%{buildroot}/ docdir=%{_datadir}/doc/ install_package_docs
%endif

# Rename unversioned binaries
mv %{buildroot}%{_bindir}/kiwi-ng %{buildroot}%{_bindir}/kiwi-ng-3

# Create symlinks for correct binaries
ln -sr %{buildroot}%{_bindir}/kiwi-ng %{buildroot}%{_bindir}/kiwi
ln -sr %{buildroot}%{_bindir}/kiwi-ng-3 %{buildroot}%{_bindir}/kiwi-ng

%if %{with pxeboot}
%ifarch x86_64
# kiwi pxeboot directory structure to be packed in kiwi-pxeboot
for i in KIWI pxelinux.cfg image upload boot; do \
    mkdir -p %{buildroot}%{buildroot}/srv/tftpboot/$i ;\
done
%fdupes %{buildroot}%{buildroot}/srv/tftpboot
%endif
%endif

%if %{with check}
%check
%pytest
%endif

%files
%{_bindir}/kiwi
%{_bindir}/kiwi-ng
%{_bindir}/kiwi-ng-3*
%{_datadir}/bash-completion/completions/kiwi-ng
%if %{with docs}
%{_mandir}/man8/kiwi*
%endif
%config(noreplace) %{_sysconfdir}/kiwi.yml
%if %{without pxeboot}
%exclude %{buildroot}/srv/tftpboot/*
%endif

# Some packages are empty
%files systemdeps-core

%if %{with containers}
%files systemdeps-containers
%endif

%files systemdeps-bootloaders

%files systemdeps-disk-images

%files systemdeps-filesystems

%files systemdeps-iso-media

%files systemdeps-image-validation

%files systemdeps

%files -n python-%{name}
%license LICENSE
%{python3_sitelib}/kiwi*/
%dir %{_datadir}/kiwi
%{_datadir}/kiwi/xsl_to_v74/

%if %{with pxeboot}
%ifarch x86_64
%files pxeboot
%license LICENSE
%{buildroot}/srv/tftpboot/*
%endif
%endif

%files -n dracut-kiwi-lib
%license LICENSE
%{_prefix}/lib/dracut/modules.d/59kiwi-lib/

%files -n dracut-kiwi-live
%license LICENSE
%{_prefix}/lib/dracut/modules.d/55kiwi-live/

%files -n dracut-kiwi-oem-dump
%license LICENSE
%{_prefix}/lib/dracut/modules.d/55kiwi-dump/
%{_prefix}/lib/dracut/modules.d/59kiwi-dump-reboot/

%files -n dracut-kiwi-oem-repart
%license LICENSE
%{_prefix}/lib/dracut/modules.d/55kiwi-repart/

%files -n dracut-kiwi-overlay
%license LICENSE
%{_prefix}/lib/dracut/modules.d/55kiwi-overlay/

%files -n dracut-kiwi-verity
%{_usr}/lib/dracut/modules.d/50kiwi-verity
%{_bindir}/kiwi-parse-verity

%changelog
%autochangelog
