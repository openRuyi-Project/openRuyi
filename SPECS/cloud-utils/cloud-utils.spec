# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cloud-utils
Version:        0.33
Release:        %autorelease
Summary:        Cloud image management utilities
License:        GPL-3.0-only
URL:            https://github.com/canonical/cloud-utils
#!RemoteAsset
Source:         https://github.com/canonical/cloud-utils/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install):  PREFIX=%{_prefix}

Requires:       %{name}-growpart
Requires:       %{name}-cloud-localds
Requires:       %{name}-write-mime-multipart
Requires:       %{name}-ec2metadata
Requires:       %{name}-resize-part-image
Requires:       %{name}-mount-image-callback
Requires:       %{name}-vcs-run

%description
This package provides a useful set of utilities for managing cloud images.
It is a meta-package that pulls in all individual utilities.

%package        cloud-localds
Summary:        A script for creating a nocloud configuration disk for cloud-init
Recommends:     tar dosfstools mtools genisoimage qemu-img

%description    cloud-localds
This package provides the cloud-localds script.

%package        write-mime-multipart
Summary:        A utilty for creating mime-multipart files

%description    write-mime-multipart
This package provides the write-mime-multipart script.

%package        ec2metadata
Summary:        A script to query and display EC2 AMI instance metadata

%description    ec2metadata
This package provides the ec2metadata script.

%package        resize-part-image
Summary:        A script for resizing cloud images
Requires:       file gzip e2fsprogs gawk tar

%description    resize-part-image
This package provides the resize-part-image script.

%package        mount-image-callback
Summary:        A script to run commands over cloud image contents
Requires:       gawk util-linux
Recommends:     qemu-img

%description    mount-image-callback
This package provides the mount-image-callback script.

%package        vcs-run
Summary:        Script to run commands over a VCS repository contents
Recommends:     git-core wget
%description    vcs-run
This package provides the vcs-run script.

%package        growpart
Summary:        A script for growing a partition
Requires:       gawk util-linux
Recommends:     lvm2

%description    growpart
This package provides the growpart script for growing a partition.

# No configure.
%conf

%install -a
rm -f %{buildroot}%{_bindir}/*ubuntu*

rm -f %{buildroot}%{_mandir}/man1/cloud-run-instances.*
rm -f %{buildroot}%{_mandir}/man1/cloud-publish-*
rm -f %{buildroot}%{_bindir}/cloud-publish-*

# No check
%check

%files
%license LICENSE
%doc ChangeLog

%files cloud-localds
%license LICENSE
%{_bindir}/cloud-localds
%{_mandir}/man1/cloud-localds.*

%files write-mime-multipart
%license LICENSE
%{_bindir}/write-mime-multipart
%{_mandir}/man1/write-mime-multipart.*

%files ec2metadata
%license LICENSE
%{_bindir}/ec2metadata

%files resize-part-image
%license LICENSE
%{_bindir}/resize-part-image
%{_mandir}/man1/resize-part-image.*

%files mount-image-callback
%license LICENSE
%{_bindir}/mount-image-callback

%files vcs-run
%license LICENSE
%{_bindir}/vcs-run

%files growpart
%license LICENSE
%{_bindir}/growpart
%{_mandir}/man1/growpart.*

%changelog
%autochangelog
