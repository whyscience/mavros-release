Name:           ros-lunar-mavros-msgs
Version:        0.21.1
Release:        0%{?dist}
Summary:        ROS mavros_msgs package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros_msgs
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-geographic-msgs
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-std-msgs
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-geographic-msgs
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-std-msgs

%description
mavros_msgs defines messages for MAVROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri Sep 22 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.21.1-0
- Autogenerated by Bloom

* Thu Sep 14 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.21.0-0
- Autogenerated by Bloom

* Mon Aug 28 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.20.1-0
- Autogenerated by Bloom

* Wed Aug 23 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.20.0-0
- Autogenerated by Bloom

* Thu May 25 2017 Vladimir Ermakov <vooon341@gmail.com> - 0.19.0-0
- Autogenerated by Bloom

